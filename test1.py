import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

db = sqlite3.connect('users.db', check_same_thread=False)
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
db.commit()

ADMIN_USER = "admin"
ADMIN_PASS = "password123"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Login successful"
    return "Invalid credentials"

@app.route('/execute', methods=['POST'])
def execute():
    command = request.form['command']
    
    os.system(command)
    return "Command executed"

if __name__ == '__main__':
    app.run(debug=True)