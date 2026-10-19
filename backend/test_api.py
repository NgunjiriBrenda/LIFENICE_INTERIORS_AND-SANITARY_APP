import requests

BASE = "http://127.0.0.1:5000/api"

login = requests.post(f"{BASE}/login", json={
    "email": "text@example.com",
    "password": "password123",

   })
token = login.json()["token"]

product  = {
    "sku": "PANEL-002 ",
    "name": "Decorative Panel",
    "category": "Interior",
    "price": 1200,
    "stock": 60,
    "description": "A decorative panel for interior design.",
}

res = requests.post(
    f"{BASE}/products",
    json=product,
    headers={"Authorization": f"Bearer {token}"},
)
print(res.status_code)
print(res.json())
