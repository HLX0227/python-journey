import json
import os

def print_roster(lst):
    for stu in lst:
        print(f"{stu['name']}:{stu['score']}分")

def average(lst):
    total = 0
    for stu in lst:
        total += stu['score']
    return total / len(lst)

def top_student(lst):
    top = lst[0]
    for stu in lst:
        if stu['score']>=top['score']:
            top = stu
    return top

def find_all(lst,name):
    results = []
    for stu in lst:
        if stu['name']==name:
            results.append(stu)
    return results

def save_data(lst,path='data.json'):
    with open(path,'w',encoding='utf-8') as f:
        json.dump(lst,f,ensure_ascii=False,indent=2)

def load_data(path='data.json'):
    with open(path,'r',encoding='utf-8') as f:
        load=json.load(f)
    return load

if os.path.exists('data.json'):
    students = load_data()
    print(f"已从文件加载{len(students)}名学生")
else:
    print("没有找到数据文件，将使用默认数据")
    students = [
        {"name": "张伟", "age": 20, "score": 85},
        {"name": "王芳", "age": 19, "score": 92},
        {"name": "李娜", "age": 21, "score": 78},
        {"name": "刘洋", "age": 20, "score": 95},
        {"name": "陈静", "age": 19, "score": 88},
    ]

print_roster(students)
print(f"平均分:{average(students):.2f}")
best = top_student(students)
print(f"最高分是:{best['name']},{best['score']}分")

results=find_all(students,input('要查谁:'))
if results:
    for stu in results:
        print(f"{stu['name']},{stu['age']}岁,{stu['score']}分")
else:
    print("没有找到")

save_data(students)
