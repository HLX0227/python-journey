import argparse
import json
import os
import sqlite3
from fileinput import close

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'todo.db')
FILE = 'todo.json'

def init_db():
    conn=sqlite3.connect(DB)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def load_tasks():
    conn=sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return rows

def cmd_add(tasks, text):
    conn=sqlite3.connect(DB)
    conn.execute('INSERT INTO tasks (text) VALUES(?)', (text,))
    conn.commit()
    conn.close()
    print(f'已添加:{text}')

def cmd_list(tasks):
    if not tasks:                # 空列表 falsy，老朋友
        print('没有任务，添加一个吧')
        return
    for row in tasks:
        mark = '✓' if row['done'] else ' '
        print(f"{row['id']}. [{mark}] {row['text']}")

def cmd_done(tasks,id):
    conn = sqlite3.connect(DB)
    cur = conn.execute('UPDATE tasks SET done = 1 WHERE id=(?)',(id,))
    conn.commit()
    conn.close()
    cur.rowcount
    if cur.rowcount == 0:
        print(f'没有id为{id}的任务')
    else:
        print(f'第{id}项已经完成')


def cmd_del(tasks,id):
    conn=sqlite3.connect(DB)
    cur = conn.execute('DELETE FROM tasks WHERE id = (?)',(id,))
    conn.commit()
    conn,close()
    if cur.rowcount == 0:
        print(f'没有id为{id}的任务')
    else:
        print(f'已删除第{id}项')

# ===== 主流程 =====
if __name__ == '__main__':
    init_db()
    parser = argparse.ArgumentParser(description='TODO 工具')
    sub = parser.add_subparsers(dest='command')
    p_add = sub.add_parser('add'); p_add.add_argument('text')
    sub.add_parser('list')
    p_done = sub.add_parser('done'); p_done.add_argument('id', type=int)
    p_del = sub.add_parser('del'); p_del.add_argument('id', type=int)
    args = parser.parse_args()

    tasks = load_tasks()


    if args.command == 'add':
        cmd_add(tasks, args.text)
    elif args.command == 'list':
        cmd_list(tasks)
    elif args.command == 'done':
        cmd_done(tasks, args.id)     # ← 你写
    elif args.command == 'del':
        cmd_del(tasks, args.id)      # ← 你写
    else:
        parser.print_help()

