import sqlite3


class SQLiteDBContextManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()  # zapamiętanie zmian w bazie
            self.conn.close()  # zamknięcie połaczenia


lista = []
db_name = "my_database.db"

with SQLiteDBContextManager(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);")
    # cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))
    # cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    # cursor.execute("INSERT INTO users (name) VALUES (?)", ("Tom",))
    select = cursor.execute("SELECT * FROM users;")
    for i in select:
        print(i)

# (1, 'John')
# (2, 'Alice')
# (3, 'Tom')
# (4, 'John')
# (5, 'Alice')
# (6, 'Tom')
