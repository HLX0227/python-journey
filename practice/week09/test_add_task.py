from blind2 import add_task
import sqlite3
import uuid

def test_add_task():
    magic = '测试专用_' + uuid.uuid4().hex[:8]

    add_task(magic)
    conn = sqlite3.connect('mydb.db')
    rows = conn.execute(
        'SELECT text, done FROM tasks WHERE text = ?', (magic,)
    ).fetchall()
    conn.close()
    assert len(rows) == 1
    assert rows[0][0] == magic
    assert rows[0][1] == 0

