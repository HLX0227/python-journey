import sqlite3



def add_task(text):
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            done INTEGER DEFAULT 0 
        )
    ''')
    cur.execute(
        'INSERT INTO tasks (text) VALUES(?)',(text,)
    )
    conn.commit()
    new_id = cur.lastrowid  # ← 关键问题在这里
    conn.close()
    return new_id

print(add_task('盲写练习'))
conn = sqlite3.connect('mydb.db')
print(conn.execute('SELECT * FROM tasks').fetchall())