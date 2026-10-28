import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'practice', 'week10', 'todo.db')

def get_done_count():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.execute('SELECT count(*) FROM tasks WHERE done = 1')
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]

print(get_done_count())