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
print("using product:", product["name"], "stock:", product["stock"])


r = requests.get(f"{BASE}/cart", headers=headers)
print("view cart:", r.status_code, r.json())

r = requests.post(f"{BASE}/cart/items", json={"product_id": pid, "quantity": 2}, headers=headers)
print("add 2:", r.status_code)


r = requests.post(f"{BASE}/cart/items", json={"product_id": pid, "quantity": 1}, headers=headers)
print("add 1 more:", r.status_code, r.json())
item_id = next(i["id"] for i in r.json()["items"] if i["product"]["id"] == pid)


r = requests.post(f"{BASE}/cart/items", json={"product_id": pid, "quantity": 9999}, headers=headers)
print("too many:", r.status_code, r.json())


r = requests.put(f"{BASE}/cart/items/{item_id}", json={"quantity": 1}, headers=headers)
print("update:", r.status_code)


r = requests.delete(f"{BASE}/cart/items/{item_id}", headers=headers)
print("remove:", r.status_code, r.json())