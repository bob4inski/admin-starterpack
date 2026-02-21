"""
add_email_and_timestamps
"""

from yoyo import step

__depends__ = {'0004_migrate_to_uuid'}

steps = [
    step(
        """
        ALTER TABLE users
            ADD COLUMN email VARCHAR(255),
            ADD COLUMN created_at TIMESTAMP DEFAULT NOW() NOT NULL,
            ADD COLUMN updated_at TIMESTAMP DEFAULT NOW() NOT NULL;

        CREATE UNIQUE INDEX idx_users_email ON users(email) WHERE email IS NOT NULL;

        -- Триггер для автообновления updated_at
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ language 'plpgsql';

        CREATE TRIGGER update_users_updated_at
            BEFORE UPDATE ON users
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
        """,
        """
        DROP TRIGGER IF EXISTS update_users_updated_at ON users;
        DROP FUNCTION IF EXISTS update_updated_at_column();
        DROP INDEX IF EXISTS idx_users_email;
        ALTER TABLE users
            DROP COLUMN IF EXISTS email,
            DROP COLUMN IF EXISTS created_at,
            DROP COLUMN IF EXISTS updated_at;
        """
    )
]
