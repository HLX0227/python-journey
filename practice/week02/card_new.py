person={
    "name":input("请输入你的名字:"),
    "age":int(input("请输入你的年龄:")),
    "home_city":input("请输入你的家乡城市:"),
    "stu_city":input("请输入你的学校所在城市:")
}

print('='*30)
for key,value in person.items():
    print(f"{key}:{value}")
print(f"明年{person['age']+1}岁")
print('='*30)
