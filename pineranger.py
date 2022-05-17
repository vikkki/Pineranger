from flask import Flask, request, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'