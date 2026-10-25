import sqlite3

conn = sqlite3.connect('mydb.db')
cur = conn.cursor()

# 建表：相当于定义"数据长什么样"
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        done INTEGER DEFAULT 0 
    )
''')

# 插入：往表里放一行
cur.execute('INSERT INTO tasks (text) VALUES(?)',('学SQL',))
cur.execute('INSERT INTO tasks (text) VALUES(?)',('买牛奶',))
cur.execute('UPDATE tasks SET done = 1 WHERE id = ?', (1,))
cur.execute('DELETE FROM tasks WHERE id = ?', (2,))
conn.commit()

# 查询：把行取回来
rows =cur.execute('SELECT * FROM tasks ').fetchall()
for row in rows:
    print(row)

conn.close()