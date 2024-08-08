import sqlite3


def get_db_schema_simple(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Отримання списку таблиць
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = {}

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        schema[table_name] = [col[1] for col in columns]

    conn.close()
    return schema


# Використання функції
db_path = 'chinook.db'
schema = get_db_schema_simple(db_path)
print(schema)