import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'week10', 'todo.db')
conn = sqlite3.connect(DB)

def count_by(conn,done_value):
    row = conn.execute('SELECT count(*) FROM tasks WHERE done = ?', (done_value,)).fetchone()
    return row[0]


print('已完成：', count_by(conn, 1))   # 预测：1
print('未完成：', count_by(conn, 0))   # 预测：1

def longest_task(conn):
    row = conn.execute(
        'SELECT text FROM tasks ORDER BY LENGTH(text) DESC LIMIT 1'
    ).fetchone()
    return row[0] if row else None      # 空表 → None，不崩
print('最长任务：', longest_task(conn))

def summary(conn):
    return {
        'done': count_by(conn,1),
        'todo': count_by(conn,0),
        'total':count_by(conn,0) + count_by(conn,1),
    }
print(summary(conn))


conn.close()
