import sqlite3

DB_NAME = "school.db"

def execute_sql_script(path: str):
    """Executes the entire SQL file."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    with open(path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    cursor.executescript(sql_script)

    conn.commit()
    conn.close()


def init_db():
    """Database initialization — launching operations.sql"""
    execute_sql_script("operations.sql")


def main():
    init_db()

if __name__ == "__main__":
    main()