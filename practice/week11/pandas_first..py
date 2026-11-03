import pandas as pd
import sqlite3
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
conn = sqlite3.connect(os.path.join(ROOT, 'practice', 'week10', 'todo.db'))
df = pd.read_sql('SELECT * FROM  tasks ' , conn)
conn.close()
# print(df)
# print(df[df['done'] == 0])
# print(df['done'].value_counts())
# print(df['text'].str.len())
print((df['done']==0).sum())
print(df[df['done'] == 1]['text'])
df['len'] = df['text'].str.len()
print(df.sort_values('len'))