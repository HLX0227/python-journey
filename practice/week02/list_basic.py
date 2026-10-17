names=["张伟","王芳","李娜","刘洋","陈静"]
print(names)

print(names[0])
print(names[-1])
print(names[-3])

print(len(names))

names.append("赵磊")
names.remove("王芳")
print(names)

for n in names:
    print(f"同学:{n}")

print(names[0:3])

print(names[::-1])

for i in names:
    print(type(i),repr(i))
