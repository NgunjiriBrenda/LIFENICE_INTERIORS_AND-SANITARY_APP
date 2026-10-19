import time
import requests

BASE = "http://127.0.0.1:5000/api"


login = requests.post(f"{BASE}/login", json={
    "email": "text@example.com",
    "password": "password123",
})
headers = {"Authorization": f"Bearer {login.json()['token']}"}


created = requests.post(f"{BASE}/products", json={
    "sku": f"TEMP-{int(time.time())}",
    "name": "Temp Chair",
    "category": "Living Room",
    "price": 5000,
    "stock": 3,
}, headers=headers)
print("create:", created.status_code)
product_id = created.json()["id"]


updated = requests.put(f"{BASE}/products/{product_id}", json={
    "price": 6500,
    "stock": 10,
}, headers=headers)
print("update:", updated.status_code, updated.json())


deleted = requests.delete(f"{BASE}/products/{product_id}", headers=headers)
print("delete:", deleted.status_code, deleted.json())


check = requests.get(f"{BASE}/products/{product_id}")
print("after delete:", check.status_code)

