# server.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Captured Credentials: {username}:{password}")
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
