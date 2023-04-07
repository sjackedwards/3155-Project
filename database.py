import sqlite3

def setup_database():
    conn = sqlite3.connect('local_app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT, api_key TEXT)''')
    conn.commit()
    conn.close()

# For the registration_test to run multiple times.
def cleanup_test_user():
    conn = sqlite3.connect('local_app.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username = 'testuser'")
    conn.commit()
    conn.close()
