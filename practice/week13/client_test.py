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


