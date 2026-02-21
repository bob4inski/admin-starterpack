"""
migrate_to_uuid
"""

from yoyo import step

__depends__ = {'0003_add_indexes'}

steps = [
    step(
        """
        -- Включаем расширение UUID
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

        -- Добавляем новую колонку
        ALTER TABLE users ADD COLUMN uuid UUID DEFAULT uuid_generate_v4();

        -- Заполняем для существующих записей
        UPDATE users SET uuid = uuid_generate_v4() WHERE uuid IS NULL;

        -- Делаем NOT NULL
        ALTER TABLE users ALTER COLUMN uuid SET NOT NULL;

        -- Удаляем старый PRIMARY KEY
        ALTER TABLE users DROP CONSTRAINT users_pkey;

        -- Переименовываем колонки
        ALTER TABLE users RENAME COLUMN id TO old_id;
        ALTER TABLE users RENAME COLUMN uuid TO id;

        -- Создаем новый PRIMARY KEY
        ALTER TABLE users ADD PRIMARY KEY (id);

        -- Удаляем старую колонку
        ALTER TABLE users DROP COLUMN old_id;
        """,
        """
        -- Rollback сложный, создаем заново таблицу с INTEGER ID
        ALTER TABLE users ADD COLUMN old_id SERIAL;
        ALTER TABLE users DROP CONSTRAINT users_pkey;
        ALTER TABLE users RENAME COLUMN id TO uuid;
        ALTER TABLE users RENAME COLUMN old_id TO id;
        ALTER TABLE users ADD PRIMARY KEY (id);
        ALTER TABLE users DROP COLUMN uuid;
        """
    )
]
