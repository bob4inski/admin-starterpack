"""
create_users_table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        # Применить (upgrade)
        """
        DROP TABLE IF EXISTS users CASCADE;
        
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            surname VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL CHECK (age >= 18 AND age <= 100),
            town VARCHAR(100) NOT NULL
        );
        """,
        # Откатить (downgrade)
        """
        DROP TABLE IF EXISTS users CASCADE;
        """
    )
]
