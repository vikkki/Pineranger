from fileinput import filename
from http.client import ImproperConnectionState
from flask import Flask, request, render_template, redirect, flash, url_for
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

def get_db_type_projects(type = "gex3"):
    conn = sqlite3.connect("notes.db")
    projects = conn.execute('select * from projects where project_type = ?', (type,)).fetchall()
    conn.close()
    return projects

def get_db_all_projects():
    conn = sqlite3.connect("notes.db")
    projects = conn.execute('select * from projects order by created desc').fetchall()
    conn.close()
    return projects

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


@app.route('/notes', methods = ("GET", "POST"))
def notes():
    conn = get_db_conn()
    notes = conn.execute('select * from posts order by created desc').fetchall()
    if request.method == 'POST':
        title = request.form['title']
        print(title)
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
            
            return redirect(url_for("notes"))
    return render_template("notes.html",data = notes)



@app.route('/notes/delete/<note_id>', methods=('POST',))
def delete_note(note_id):
    post = get_db_note(note_id)
    conn = get_db_conn()
    conn.execute('delete from posts where id = ?', (note_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("notes"))

@app.route('/projects', methods = ("GET",))
def all_projects():
    projects = get_db_all_projects()
    return render_template("projects.html",data = projects)



json_test = '[{"mm,aa,ww,ss":1,"a":233},{"mm,aa,ww,ss":2,"a":2333}]'
