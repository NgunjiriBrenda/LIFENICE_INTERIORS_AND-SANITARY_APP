from flask import Flask
from flask_cors import CORS
from database import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lifenice.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET"] = "dev-secret-change-me"

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    db.init_app(app)

    with app.app_context():
        import models  
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)