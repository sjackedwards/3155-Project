import sqlite3
import hashlib
import re

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


# Password requirements
# TODO: Make this work better with registration. e.g. say what failed in the password registration.

def check_password_requirements(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    return True




def register(username, password):
    if not check_password_requirements(password):
        return False, "Password does not meet the requirements."

    conn = sqlite3.connect("local_app.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if cursor.fetchone() is not None:
        cursor.close()
        conn.close()
        return False, "Username already exists."

    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

    cursor.close()
    conn.close()
    return True, "User registered successfully."


def login(username, password):
    db_conn = sqlite3.connect("local_app.db")
    cursor = db_conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    db_pass = cursor.fetchone()
    cursor.close()
    db_conn.close()

    if db_pass is None:
        return None

    # Checks the hashed password in the database against user input.
    stored_password = db_pass[0]
    hashed_password = hash_password(password)

    if stored_password == hashed_password:
        return username
    else:
        return None


###   TODO: I want to implement some type of error reporting. If the user puts in an empty password,
###           the dialog box says 'empty password'. Commit comment


    