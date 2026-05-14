from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# HARDCODED SECRET (Intentional vulnerability for Gitleaks to catch)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Vulnerable DevSecOps Test App",
        "status": "running"
    })

@app.route('/users')
def get_users():
    # SQL Injection Vulnerability (Intentional for SonarQube to catch)
    user_id = "1 OR 1=1"
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # Bad practice: using string interpolation for SQL queries
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    users = cursor.fetchall()
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
