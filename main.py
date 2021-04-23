from flask import Flask, render_template
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation', methods=['POST'])
def login_validation():
    return "...."

if __name__ == "__main__":
    app.run(debug=True)