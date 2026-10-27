import sqlite3


def del_task(task_id):
     conn=sqlite3.connect('mydb.db')
     cur=conn.cursor()
     cur.execute('DELETE FROM tasks WHERE id=(?)',(task_id,))
     deleted = cur.rowcount
     conn.commit()
     conn.close()
     return deleted
# print(del_task('999'))
print(del_task('1'))
