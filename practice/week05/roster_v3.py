import json
import os
from os import remove

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
    try:
        with open(path,'r',encoding='utf-8') as f:
            return(json.load(f))
    except FileNotFoundError:
        print("没有找到数据文件，将使用空名单")
        return []
    except json.JSONDecodeError:
        print("数据文件有误，将使用空名单")
        return []

def add_student(lst,name,age,score):
    new={'name':name,'age':age,'score':score}
    lst.append(new)
    return new

def delete_student(lst,name):
    kept=[]
    for i in lst:
        if i['name']!=name:
            kept.append(i)
    return kept

def update_score(lst,name,new_score):
    for i in lst:
        if i['name']==name:
            i['score']=new_score
            return True
    return False


students = load_data()
if not students:
    students = [
        {"name": "张伟", "age": 20, "score": 85},
        {"name": "王芳", "age": 19, "score": 92},
        {"name": "李娜", "age": 21, "score": 78},
        {"name": "刘洋", "age": 20, "score": 95},
        {"name": "陈静", "age": 19, "score": 88},
    ]
    save_data(students)
    print('数据为空，已恢复为默认名单')

students=delete_student(students,input('要删谁:'))
#
#
# print_roster(students)
# print(f"平均分:{average(students):.2f}")
# best = top_student(students)
# print(f"最高分是:{best['name']},{best['score']}分")

results=find_all(students,input('要查谁:'))
if results:
    for stu in results:
        print(f"{stu['name']},{stu['age']}岁,{stu['score']}分")
else:
    print("没有找到")

save_data(students)
