import argparse

parser = argparse.ArgumentParser(description='TODO 工具')
sub = parser.add_subparsers(dest='command')      # dest 决定动作存进 args.command

# 子命令：add
p_add = sub.add_parser('add', help='添加任务')
p_add.add_argument('text', help='任务内容')

# 子命令：list
sub.add_parser('list', help='列出所有任务')

# 子命令：done
p_done = sub.add_parser('done', help='完成任务')
p_done.add_argument('id', type=int, help='任务编号')

# 子命令：del
p_del = sub.add_parser('del',help='删除任务')
p_del.add_argument('id', type=int, help='任务编号')

args = parser.parse_args()

# 根据 args.command 决定干哪件事
if args.command == 'add':
    print(f'要添加：{args.text}')
elif args.command == 'list':
    print('要列出所有任务')
elif args.command == 'done':
    print(f'要完成第 {args.id} 项')
elif args.command == 'del':
    print(f'要删除第{args.id}项')
else:
    print('请告诉我你想干什么，用 --help 看用法')