import requests

BASE = "http://127.0.0.1:5000/api"

login = requests.post(f"{BASE}/login", json={
    "email": "text@example.com",
    "password": "password123",
})
headers = {"Authorization": f"Bearer {login.json()['token']}"}


products = requests.get(f"{BASE}/products").json()
product = next(p for p in products if p["stock"] >= 2)
pid = product["id"]
print("stock before:", product["stock"])


shipping = {
    "shipping_name": "Test User",
    "shipping_address": "123 Test Street",
    "shipping_city": "Nairobi",
    "shipping_zip": "00100",
}
r = requests.post(f"{BASE}/checkout", json=shipping, headers=headers)
print("empty cart:", r.status_code, r.json())


requests.post(f"{BASE}/cart/items", json={"product_id": pid, "quantity": 2}, headers=headers)
r = requests.post(f"{BASE}/checkout", json=shipping, headers=headers)
print("checkout:", r.status_code, r.json())
order_id = r.json()["id"]

print("cart after:", requests.get(f"{BASE}/cart", headers=headers).json())


after = requests.get(f"{BASE}/products/{pid}").json()
print("stock after:", after["stock"])


print("my orders:", requests.get(f"{BASE}/orders", headers=headers).status_code)
print("one order:", requests.get(f"{BASE}/orders/{order_id}", headers=headers).status_code)