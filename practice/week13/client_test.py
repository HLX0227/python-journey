import requests

BASE =  'http://127.0.0.1:5000'

r = requests.post(BASE+'/tasks',json = {'text':'POST 测试'})
print(r.status_code,r.json())

r = requests.post(BASE+'/tasks',json = {})
print(r.status_code,r.json())

r = requests.post(BASE+'/tasks',json = {'text':'   '})
print(r.status_code,r.json())

r = requests.get(BASE+'/')
print(r.status_code,r.text)

r = requests.get(BASE+'/tasks')
print(r.status_code,r.text)

r = requests.delete(BASE + '/tasks/8')     # POST 测试之一
print(r.status_code, r.json())             # 期望 200
r = requests.delete(BASE + '/tasks/8')     # 再删一次同一个
print(r.status_code, r.json())             # 期望 ??? ← 先猜再跑

r= requests.put(BASE + '/tasks/3',json = {'text':'c'})
print(r.status_code, r.json())

r = requests.put(BASE + '/tasks/999',json = {'text':'x'})
print(r.status_code, r.json())

r = requests.put(BASE + '/tasks/3',json = {})
print(r.status_code, r.json())

# 清掉剩下的 POST 测试
r = requests.get(BASE + '/tasks')
victims = [t['id'] for t in r.json() if t['text'] == 'POST 测试']
print('待清:', victims)
for tid in victims:
    print(tid, requests.delete(BASE + f'/tasks/{tid}').status_code)
print('剩余:', len(requests.get(BASE + '/tasks').json()))

# 终验
r = requests.get(BASE+'/tasks')
print(r.status_code,len(r.json()))

# PATCH 翻转完成状态
r = requests.patch(BASE + '/tasks/3/done')
print(r.status_code, r.json())      # 期望 200，done 从 1 变 0（或反过来）

r = requests.patch(BASE + '/tasks/3/done')
print(r.status_code, r.json())      # 再翻一次，回到原状态 ← 翻转的闭环

r = requests.patch(BASE + '/tasks/999/done')
print(r.status_code, r.json())      # 期望 404，查无此任务

for tid in (22, 23):
    print(tid, requests.delete(f'http://127.0.0.1:5000/tasks/{tid}').status_code)