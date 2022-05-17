from http.client import ImproperConnectionState
from flask import Flask, request, render_template
from markupsafe import escape
from psutil import cpu_percent, virtual_memory
import os

def get_cpu_percent():
    return cpu_percent()

def get_memory_used():
    return virtual_memory()[2]

app = Flask(__name__)

@app.route('/')
def index():
    data = {"cpu_percent": get_cpu_percent(),
    "memory_used" : get_memory_used()}
    return render_template("index.html", data=data)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
