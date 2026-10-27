student={"name":"胡乐轩","age":"19","city":"杭州"}
# print(student)
print(student['name'])
print(student['age'])
print(student['city'])

student['age']=20
student['major']='计算机科学与技术'
# print(student)

# for key in student:
#     print(key)

for key,value in student.items():
    print(f'{key}:{value}')

print(student.get('phone','未填写'))


