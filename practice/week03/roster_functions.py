students = [
    {"name":"张伟","age":20,"score":85},
    {"name":"王芳","age":19,"score":92},
    {"name":"李娜","age":21,"score":78},
    {"name":"刘洋","age":20,"score":95},
    {"name":"陈静","age":19,"score":88},
]

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


print_roster(students)
print(f"平均分:{average(students)}")
best = top_student(students)
print(f"最高分是:{best['name']},{best['score']}分")

results=find_all(students,input('要查谁:'))
if results:
    for stu in results:
        print(f"{stu['name']},{stu['age']}岁,{stu['score']}分")
else:
    print("没有找到")

