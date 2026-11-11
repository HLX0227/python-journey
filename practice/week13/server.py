from flask import Flask,jsonify,request
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

@app.route('/tasks', methods=['GET', 'POST', ])
def tasks():
    # 处理 POST 请求：创建新任务
    if request.method == 'POST':
        # 解析请求体中的 JSON 数据，silent=True 表示解析失败时返回 None 而非抛出异常
        data = request.get_json(silent=True)
        # 校验：JSON 为空，或 text 字段不存在，或 text 内容为空白字符串，均返回 400 错误
        if not data or not data.get('text','').strip():
            return jsonify({'error':'任务内容不能为空'}), 400
        conn = sqlite3.connect(todo_db.DB)
        cur = conn.execute('INSERT INTO tasks (text) VALUES (?)', (data['text'].strip(),))
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        return jsonify({'id': new_id, 'text': data['text'].strip()}),201
    conn = sqlite3.connect(todo_db.DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    # 将每行转为字典后序列化为 JSON 数组返回
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
@app.route('/search')
def search():
    kw = request.args.get('keyword', '')
    conn = sqlite3.connect(todo_db.DB)
    conn.row_factory = sqlite3.Row
    # 使用 LIKE 模糊匹配搜索包含关键词的任务
    rows = conn.execute('SELECT * FROM tasks WHERE text like ?', ('%' + kw + '%',)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def del_task_api(task_id):
    conn = sqlite3.connect(todo_db.DB)
    conn.row_factory = sqlite3.Row
    cur = conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    if deleted == 0:
        return jsonify({'error': '任务不存在'}), 404
    return jsonify({'deleted': deleted})
    # 提示：删了几行？rowcount == 0 说明什么？

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json(silent=True)
    if not data or not data.get('text', '').strip():
        return jsonify({'error': '任务内容不能为空'}), 400      # 安检在门口
    conn = sqlite3.connect(todo_db.DB)
    cur = conn.execute('UPDATE tasks SET text = ? WHERE id = ?',
                       (data['text'].strip(), task_id))
    conn.commit()
    changed = cur.rowcount                                      # cur 记账，
    conn.close()
    if changed == 0:
        return jsonify({'error': '任务不存在'}), 404            # 查户口在里屋
    return jsonify({'id': task_id, 'text': data['text'].strip()})

if __name__ == '__main__':
    app.run(debug=True)




