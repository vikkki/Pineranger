from http.client import ImproperConnectionState
from flask import Flask, request, render_template, redirect
from markupsafe import escape
from psutil import cpu_percent, virtual_memory
import json
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = "today's cake is perfect"

def get_db_conn():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_db_note(note_id):
    conn = sqlite3.connect("notes.db")
    post = conn.execute('select * from posts where id = ?', (note_id,)).fetchone()
    return post

def get_cpu_percent():
    return cpu_percent()

def get_memory_used():
    return virtual_memory()[2]



@app.route('/')
def index():
    data = {"cpu_percent": get_cpu_percent(),
    "memory_used" : get_memory_used()}
    return render_template("index.html", data=data)

@app.route('/history_line_data')
def get_history_line_data():
    # show the user profile for that user
    return json_test

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/notes')
def notes():
    conn = get_db_conn()
    notes = conn.execute('select * from posts order by created desc').fetchall()
    return render_template("notes.html",data = notes)

@app.route("/notes/new", methods = ("GET", "POST"))
def new_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required ')
        elif not content:
            flash('Content is required ')
        else:
            conn = get_db_conn()
            conn.execute('insert into posts (title, content) values (?, ?)', (title, content))
            flash("Submit success!")
            conn.commit()
            conn.close()
            
            return redirect(url_for("index"))

    return render_template("new.html")

@app.route('/notes/delete/<note_id>', methods=('POST',))
def delete_note(note_id):
    post = get_db_note(note_id)
    conn = get_db_conn()
    conn.execute('delete from posts where id = ?', (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("notes"))


json_test = '[{"mm,aa,ww,ss":1,"a":233},{"mm,aa,ww,ss":2,"a":2333}]'
