from flask import Blueprint, request, jsonify
from database import db
from models import Product, Cart, CartItem
from routers.auth import token_required

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