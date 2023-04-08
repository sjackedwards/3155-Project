import sqlite3
import hashlib
import re

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def check_password_requirements(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    return True




def register(username, password, api_key):
    hashed_password = hash_password(password)

    db_conn = sqlite3.connect("local_app.db")
    cursor = db_conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password, api_key) VALUES (?, ?, ?)", (username, hashed_password, api_key))
        db_conn.commit()
        success = True
        message = "User successfully registered."
    except sqlite3.IntegrityError:
        success = False
        message = "Username already exists."
    finally:
        cursor.close()
        db_conn.close()

    return success, message



def login(username, password):
    db_conn = sqlite3.connect("local_app.db")
    cursor = db_conn.cursor()

    cursor.execute("SELECT password, api_key FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    cursor.close()
    db_conn.close()

    if result is None:
        return None, None

    stored_password, api_key = result
    hashed_password = hash_password(password)

    if stored_password == hashed_password:
        return username, api_key
    else:
        return None, None

