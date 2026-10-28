import argparse
import os
import sqlite3

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

def load_tasks(conn):
     return conn.execute('SELECT * FROM tasks').fetchall()

def cmd_add(conn, text):
    conn.execute('INSERT INTO tasks (text) VALUES(?)', (text,))
    conn.commit()
    print(f'已添加:{text}')

def cmd_list(tasks):
    if not tasks:                # 空列表 falsy，老朋友
        print('没有任务，添加一个吧')
        return
    for row in tasks:
        mark = '✓' if row['done'] else ' '
        print(f"{row['id']}. [{mark}] {row['text']}")

def cmd_done(conn,id):
    cur = conn.execute('UPDATE tasks SET done = 1 WHERE id=(?)',(id,))
    conn.commit()
    if cur.rowcount == 0:
        print(f'没有id为{id}的任务')
    else:
        print(f'第{id}项已经完成')


def cmd_del(conn,id):
    cur = conn.execute('DELETE FROM tasks WHERE id = (?)',(id,))
    conn.commit()
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
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row


    if args.command == 'add':
        cmd_add(conn, args.text)
    elif args.command == 'list':
        cmd_list(load_tasks(conn))
    elif args.command == 'done':
        cmd_done(conn, args.id)     # ← 你写
    elif args.command == 'del':
        cmd_del(conn, args.id)      # ← 你写
    else:
        parser.print_help()
    conn.close()
