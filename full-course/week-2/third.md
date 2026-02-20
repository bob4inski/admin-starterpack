## Небольшое введение во flask и CRUD

1. Как ваш запрос идет от ноута до БД?

Браузер → Nginx (веб-сервер) → Gunicorn/uWSGI (WSGI-сервер) → Flask/Django (приложение) → PostgreSQL (база данных)

1. Что такое REST
GET    /users/1     - Получить
POST   /users       - Создать
PUT    /users/1     - Обновить
DELETE /users/1     - Удалить


1. Что такое фласк
Это питонячка которая позволяет создавать веб-приложения

2. Что такое CRUD
Create - Post
Read - GET
Update - PUT/PATCH
Delete - DELETE

2. Правильный менеджиннг подключениями (pgbouncer или на стороне приложения)
3. Иньекции
4. Кеширование

5. python3 venv
5. запуск кода под uwsgithird.md

