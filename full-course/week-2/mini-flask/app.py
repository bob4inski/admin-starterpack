import os
import redis
import psycopg2

from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify

app = Flask(__name__)

# Получаем переменные окружения
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_NAME = os.getenv("PG_NAME", "mydb")
PG_USER = os.getenv("PG_USER", "user")
PG_PASSWORD = os.getenv("PG_PASSWORD", "password")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_DB = os.getenv("REDIS_DB", "0")


def get_pg_connection() -> psycopg2.extensions.connection:
    """Создает подключение к базе данных"""
    conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, database=PG_NAME, user=PG_USER, password=PG_PASSWORD)
    return conn


# def get_redis_connection() -> redis.Redis:
#     """Создает подключение к базе данных"""
#     conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
#     return conn

# def get_data_from_redis(user_id: str) -> dict:
#     conn = get_redis_connection()
#     user = conn.get(user_id)
#     if user:
#         return user
#     else:
#         return get_data_from_pg(user_id)


def get_data_from_pg(query: str) -> dict:
    conn = get_pg_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data


@app.route("/user/get", methods=["GET"])
def get_user():
    """Получает пользователя по ID"""
    user_id = request.args.get("id")

    # if not user_id:
    #     return jsonify({"error": "ID parameter is required"}), 400
    # try:

    query = f"SELECT * FROM users WHERE id = {user_id}"
    user = get_data_from_pg(query)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

    # except Exception as e:
    #     return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    """Проверка здоровья приложения"""
    try:
        conn = get_pg_connection()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
