import argparse
import json

FILE = 'todo.json'

def load_tasks():
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('数据损坏，从空列表开始')
        return []

def save_tasks(tasks):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# ===== 下面两个分支我示范，你抄作业 =====

def cmd_add(tasks, text):
    tasks.append({'text': text, 'done': False})
    print(f'已添加：{text}（现在共 {len(tasks)} 项）')

def cmd_list(tasks):
    if not tasks:                # 空列表 falsy，老朋友
        print('没有任务，添加一个吧')
        return
    for i, t in enumerate(tasks, start=1):
        mark = '✓' if t['done'] else ' '
        print(f'{i}. [{mark}] {t["text"]}')

def cmd_done(tasks,id):
    if id>0 and id<=len(tasks):
        tasks[id-1]['done']=True
        print(f'第{id}项已完成')
    else:
        print('无效的编号')

def cmd_del(tasks,id):
    if id>0 and id<=len(tasks):
        del tasks[id-1]
        print(f'已删除第{id}项')
    else:
        print('无效的编号')

# ===== 主流程 =====
if __name__ == '__main__':
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

    save_tasks(tasks)                # 开头加载、结尾存盘，上周的骨架
