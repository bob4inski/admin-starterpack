"""
seed_users_data
"""

from yoyo import step

__depends__ = {'0001_create_users_table'}

steps = [
    step(
        """
        INSERT INTO users (name, surname, age, town)
        SELECT
            (ARRAY['John', 'Mike', 'Tom', 'Alex', 'Chris'])[floor(random() * 5 + 1)],
            (ARRAY['Smith', 'Brown', 'Johnson', 'Taylor', 'Davis'])[floor(random() * 5 + 1)],
            floor(random() * 50 + 20)::int,
            (ARRAY['New York', 'Chicago', 'Boston', 'Seattle', 'Austin'])[floor(random() * 5 + 1)]
        FROM generate_series(1, 100) AS i;
        """,
        """
        DELETE FROM users;
        """
    )
]
