import os
import sqlite3
from flask import Flask, request, abort

import secrets

app = Flask(__name__)

def get_db():
    db = getattr(app, '_database', None)
    if db is None:
        db = sqlite3.connect('users.db', check_same_thread=False)
        db.execute("PRAGMA foreign_keys = ON")
        app._database = db
    return db

def init_db():
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
    db.commit()

init_db()

ADMIN_USER = "admin"
ADMIN_PASS = None
ADMIN_TOKEN = secrets.token_urlsafe(32)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        return "Login successful"
    abort(401, "Invalid credentials")

@app.route('/execute', methods=['POST'])
def execute():
    token = request.form.get('token', '')
    command = request.form.get('command', '')

    if token != ADMIN_TOKEN:
        abort(403, "Forbidden")

    allowed_commands = {'ls', 'whoami', 'date'}
    if command not in allowed_commands:
        abort(400, "Invalid command")

    result = os.popen(command).read()
    return result

if __name__ == '__main__':
    app.run(debug=False)