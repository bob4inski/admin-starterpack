import os
import sys
import json
import logging

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

# Настройка логирования

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)


PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_NAME = os.getenv("PG_NAME", "database")
PG_USER = os.getenv("PG_USER", "user")
PG_PASSWORD = os.getenv("PG_PASSWORD", "password")

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    town = db.Column(db.String(100), nullable=False)


@app.route("/", methods=["GET"])
def home():
    logger.info("API работает")
    return {"message": "API работает!", "routes": ["GET /user/<id>", "PUT /user/<id>/name"]}


@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Получить пользователя по ID"""
    user = User.query.get_or_404(user_id)
    data = {"id": user.id, "name": user.name, "surname": user.surname, "age": user.age, "town": user.town}
    logger.info(f"Got user: {data}")
    response = app.response_class(
        response=json.dumps(data, ensure_ascii=False, indent=4), status=200, mimetype="application/json"
    )
    logger.debug(f"Send response: {response}")
    return response


@app.route("/user/<int:user_id>/name", methods=["PUT"])
def update_user_name(user_id):
    """Обновить имя пользователя по ID"""
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    # Обновляем имя
    user.name = data["name"]
    db.session.commit()
    logger.debug(f"Updated user: {user}")
    response = app.response_class(
        response=json.dumps(
            {"message": "Имя обновлено", "id": user.id, "name": user.name}, ensure_ascii=False, indent=4
        ),
        status=200,
        mimetype="application/json",
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5005)
