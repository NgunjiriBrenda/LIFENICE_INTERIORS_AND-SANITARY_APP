import jwt
from datetime import datetime, timedelta
from flask import current_app

def create_token(user_id, days=7):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=days),

    }
    return jwt.encode(payload, current_app.config["JWT_SECRET"], algorithm ="HS256")

def decode_token(token):

    return jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=["HS256"])