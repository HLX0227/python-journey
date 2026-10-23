import argparse
parser = argparse.ArgumentParser(description='我的第一个命令行工具')
parser.add_argument('name',help='你的名字')
parser.add_argument('--age',type=int,default=18,help='年龄，不填默认18')

args = parser.parse_args()

print(f'你好,{args.name}! 你今年{args.age}岁')
