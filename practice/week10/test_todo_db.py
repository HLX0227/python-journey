import sqlite3
import todo_db


def fresh_db():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.execute('''CREATE TABLE tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        done INTEGER DEFAULT 0
    )
    ''')
    return conn

def test_add():
    conn = fresh_db()
    todo_db.cmd_add(conn, '测试任务')
    row = conn.execute('SELECT text FROM tasks WHERE text=?', ('测试任务',)).fetchone()
    assert row is not None
    assert len(row) == 1

def test_done():
    conn = fresh_db()
    todo_db.cmd_add(conn, '真真任务')
    todo_db.cmd_done(conn,1)
    row = conn.execute('SELECT done FROM tasks').fetchone()
    assert row['done'] == 1

def test_done_wrong_id():
    conn = fresh_db()
    todo_db.cmd_add(conn, '真任务')
    todo_db.cmd_done(conn,99)
    row = conn.execute('SELECT done FROM tasks').fetchone()
    assert row['done'] == 0