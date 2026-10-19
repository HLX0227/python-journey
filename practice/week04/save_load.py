import json

students=[
    {'name':"张伟",'age':20,'score':85},
    {'name':"王芳",'age':19,'score':92},
]
# 写入：把 Python 数据变成文件
with open('data.json','w',encoding='utf-8') as f:
    json.dump(students,f,ensure_ascii=False,indent=2)

# 读出：把文件变回 Python 数据
with open('data.json','r',encoding='utf-8') as f:
    loaded=json.load(f)

print(type(loaded))
print(loaded[0]['name'])


