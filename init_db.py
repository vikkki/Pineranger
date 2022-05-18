import sqlite3

conn = sqlite3.connect("notes.db")

with open("db.sql") as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Compress Lu fastq files', 'Google Drive Link')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Learn flask', 'And learn SQL')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Check Visium FFPE slides', 'Confirm tissue blocks')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('GeoMx', 'Start ealier')
            )

cur.execute("INSERT INTO projects (title, project_type) VALUES (?, ?)",
            ('Lozito Lab 20220512', 'gex3')
            )
cur.execute("INSERT INTO projects (title, project_type) VALUES (?, ?)",
            ('Lozito Lab 20220519', 'gex3')
            )
cur.execute("INSERT INTO projects (title, project_type) VALUES (?, ?)",
            ('Lozito Lab 20210309', 'visium')
            )
cur.execute("INSERT INTO projects (title, project_type) VALUES (?, ?)",
            ('Lu lab 20220102', 'gex3')
            )

conn.commit()
conn.close()