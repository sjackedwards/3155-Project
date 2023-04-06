import sqlite3

DB_FILE = 'local_app.db'

# Credit to my co-worker who greatly helped me set this database up.
def setup_database():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

# For the registration_test to run multiple times.
def cleanup_test_user():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username = 'testuser'")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
