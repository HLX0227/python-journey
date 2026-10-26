import sqlite3
import os
#让数据库跟着脚本走而不是跟着你站的位置走
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shop.db')
conn = sqlite3.connect(DB)      # 原来是 connect('shop.db')
cur = conn.cursor()

# 表1：用户
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
)
''')

# 表2：订单——注意 user_id，它"指向"users 表的 id
cur.execute('''
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER ,
item TEXT,
price INTEGER
)
''')
cur.execute('INSERT INTO users(name) VALUES(?)',('胡乐轩',))
cur.execute('INSERT INTO users(name) VALUES(?)',('张伟',))
u1 = cur.lastrowid-1

# 给胡乐轩下两单、张伟下一单（自己写三条 INSERT，user_id 填对）
cur.execute('INSERT INTO orders(user_id,item,price) VALUES(?,?,?)',(1,'键盘',200,))
cur.execute('INSERT INTO orders(user_id,item,price) VALUES(?,?,?)',(1,'鼠标',50,))
cur.execute('INSERT INTO orders(user_id,item,price) VALUES(?,?,?)',(2,'显示器',1000,))
cur.execute('UPDATE users SET name = ? WHERE id = ?',('小胡',1))
rows = cur.execute('''SELECT users.name,orders.item,orders.price FROM orders JOIN users ON user_id = users.id
''').fetchall()

conn.commit()
for r in rows:
    print(r)
print(cur.execute('PRAGMA table_info(orders)').fetchall())#验证


conn.close()
