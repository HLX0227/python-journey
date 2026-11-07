from flask import Flask,jsonify
import sqlite3
import sys
import os
sys.path.append(os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'week10'))
import todo_db


app = Flask(__name__)
app.json.ensure_ascii = False
@app.route('/')
def home():
    return '你好，这是我的第一个服务器'

@app.route('/tasks')
def tasks():
    conn = sqlite3.connect(todo_db.DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/tasks/<int:task_id>')
def one_task(task_id):
    conn = sqlite3.connect(todo_db.DB)
    conn.row_factory = sqlite3.Row
    row = conn.execute('SELECT * FROM tasks where id = ?',(task_id,)).fetchone()
    conn.close()
    if row is None:
        return jsonify({'error': '任务不存在'}), 404
    return jsonify(dict(row))



if __name__ == '__main__':
    app.run(debug=True)




