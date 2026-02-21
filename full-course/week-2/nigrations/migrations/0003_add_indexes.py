"""
add_indexes
"""

from yoyo import step

__depends__ = {'0002_seed_users_data'}

steps = [
    step(
        """
        CREATE INDEX idx_users_name ON users(name);
        CREATE INDEX idx_users_surname ON users(surname);
        CREATE INDEX idx_users_name_surname ON users(name, surname);
        CREATE INDEX idx_users_town ON users(town);
        """,
        """
        DROP INDEX IF EXISTS idx_users_town;
        DROP INDEX IF EXISTS idx_users_name_surname;
        DROP INDEX IF EXISTS idx_users_surname;
        DROP INDEX IF EXISTS idx_users_name;
        """
    )
]
