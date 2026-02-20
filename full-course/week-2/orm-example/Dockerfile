FROM python:3.11-slim

WORKDIR /app

# Создаем непривилегированного пользователя
RUN useradd -m -u 1000 appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown -R appuser:appuser /app

USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
