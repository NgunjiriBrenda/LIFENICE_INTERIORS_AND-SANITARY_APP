from flask import Blueprint, request, jsonify
from database import db
from models import Product, Cart, CartItem
from routers.auth import token_required

from models import Product, Cart, CartItem, Order, OrderItem

orders_bp = Blueprint("orders", __name__)


def get_or_create_cart(user):
    cart = Cart.query.filter_by(user_id=user.id).first()
    if not cart:
        cart = Cart(user_id=user.id)
        db.session.add(cart)
        db.session.commit()
    return cart


def cart_response(cart):
    data = cart.to_dict()
    data["total"] = sum(i.product.price * i.quantity for i in cart.items)
    return data


@orders_bp.route("/cart", methods=["GET"])
@token_required
def view_cart(current_user):
    cart = get_or_create_cart(current_user)
    return jsonify(cart_response(cart)), 200


@orders_bp.route("/cart/items", methods=["POST"])
@token_required
def add_to_cart(current_user):
    data = request.get_json(silent=True) or {}
    product_id = data.get("product_id")
    if not product_id:
        return jsonify({"error": "product_id is required"}), 400

    try:
        quantity = int(data.get("quantity", 1))
    except (TypeError, ValueError):
        return jsonify({"error": "quantity must be a number"}), 400
    if quantity < 1:
        return jsonify({"error": "quantity must be at least 1"}), 400

    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart = get_or_create_cart(current_user)
    item = CartItem.query.filter_by(cart_id=cart.id, product_id=product.id).first()

    new_quantity = quantity + (item.quantity if item else 0)
    if new_quantity > product.stock:
        return jsonify({"error": f"Only {product.stock} in stock"}), 400

    if item:
        item.quantity = new_quantity
    else:
        db.session.add(CartItem(cart_id=cart.id, product_id=product.id, quantity=new_quantity))
    db.session.commit()

    return jsonify(cart_response(cart)), 201


@orders_bp.route("/cart/items/<int:item_id>", methods=["PUT"])
@token_required
def update_cart_item(current_user, item_id):
    cart = get_or_create_cart(current_user)
    item = CartItem.query.filter_by(id=item_id, cart_id=cart.id).first()
    if not item:
        return jsonify({"error": "Item not found in your cart"}), 404

    data = request.get_json(silent=True) or {}
    try:
        quantity = int(data.get("quantity"))
    except (TypeError, ValueError):
        return jsonify({"error": "quantity must be a number"}), 400
    if quantity < 1:
        return jsonify({"error": "quantity must be at least 1"}), 400
    if quantity > item.product.stock:
        return jsonify({"error": f"Only {item.product.stock} in stock"}), 400

    item.quantity = quantity
    db.session.commit()
    return jsonify(cart_response(cart)), 200


@orders_bp.route("/cart/items/<int:item_id>", methods=["DELETE"])
@token_required
def remove_cart_item(current_user, item_id):
    cart = get_or_create_cart(current_user)
    item = CartItem.query.filter_by(id=item_id, cart_id=cart.id).first()
    if not item:
        return jsonify({"error": "Item not found in your cart"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify(cart_response(cart)), 200


@orders_bp.route("/checkout", methods=["POST"])
@token_required
def checkout(current_user):
    data = request.get_json(silent=True) or {}
    shipping_name = (data.get("shipping_name") or "").strip()
    shipping_address = (data.get("shipping_address") or "").strip()
    shipping_city = (data.get("shipping_city") or "").strip()
    shipping_zip = (data.get("shipping_zip") or "").strip()

    if not shipping_name or not shipping_address or not shipping_city:
        return jsonify({"error": "shipping_name, shipping_address and shipping_city are required"}), 400

    cart = get_or_create_cart(current_user)
    if not cart.items:
        return jsonify({"error": "Your cart is empty"}), 400


    for item in cart.items:
        if item.quantity > item.product.stock:
            return jsonify({"error": f"Only {item.product.stock} of {item.product.name} in stock"}), 400

    try:
        order = Order(
            user_id=current_user.id,
            shipping_name=shipping_name,
            shipping_address=shipping_address,
            shipping_city=shipping_city,
            shipping_zip=shipping_zip,
            total=sum(i.product.price * i.quantity for i in cart.items),
        )
        db.session.add(order)

        for item in list(cart.items):
            db.session.add(OrderItem(
                order=order,
                product_id=item.product_id,
                quantity=item.quantity,
                price_at_purchase=item.product.price,
            ))
            item.product.stock -= item.quantity
            db.session.delete(item)

        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"error": "Could not place order"}), 500

    return jsonify(order.to_dict()), 201


@orders_bp.route("/orders", methods=["GET"])
@token_required
def list_orders(current_user):
    orders = (
        Order.query.filter_by(user_id=current_user.id)
        .order_by(Order.created_at.desc())
        .all()
    )
    return jsonify([o.to_dict() for o in orders]), 200


@orders_bp.route("/orders/<int:order_id>", methods=["GET"])
@token_required
def get_order(current_user, order_id):
    order = Order.query.filter_by(id=order_id, user_id=current_user.id).first()
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict()), 200