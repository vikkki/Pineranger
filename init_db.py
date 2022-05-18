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

conn.commit()
conn.close()