import json
import sqlite3
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
old = json.load(open(os.path.join(ROOT, 'todo.json'), encoding='utf-8'))
conn = sqlite3.connect(os.path.join(ROOT, 'practice', 'week10', 'todo.db'))
conn.row_factory = sqlite3.Row

existing = {row['text'] for row in conn.execute('SELECT text FROM tasks')}  # 集合：谁已在家
moved = 0
for t in old:
    if t['text'] not in existing:
        conn.execute('INSERT INTO tasks (text, done) VALUES (?, ?)',
                     (t['text'], 1 if t['done'] else 0))
        moved += 1
conn.commit()
conn.close()
print(f'搬家完成，新增 {moved} 条')