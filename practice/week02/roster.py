students = [
    {"name":"张伟","age":20,"score":85},
    {"name":"王芳","age":19,"score":92},
    {"name":"李娜","age":21,"score":78},
    {"name":"刘洋","age":20,"score":95},
    {"name":"陈静","age":19,"score":88},
]

s=0
for i in students:
    print(f"{i['name']}:{i['score']}分")
    s+=i["score"]

Average_s=s/len(students)
print(Average_s)

top = students[0]
for x in students:
    if x["score"]>=top["score"]:
        top = x
print(f"最高分{top['name']},{top['score']}分")

target=input("要查谁:")
found=0
for n in students:
    if target==n["name"]:
        print(f"{n['name']},{n['age']}岁,{n['score']}分")
        found=1

if found==0:
    print("未查找到该人物")




