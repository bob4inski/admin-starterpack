import json

from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/date", methods=["POST"])
def update_data():
    # Десериализация - получаем JSON из запроса
    data = request.get_json()

    # Подменяем поле 'timestamp' на текущее время
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["city"] = "test"
    # Сериализация - отправляем JSON обратно
    response = app.response_class(
        response=json.dumps(data, ensure_ascii=False, indent=4), status=200, mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5100)
