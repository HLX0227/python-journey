def top_by(lst, key):
    top = None
    for item in lst:
        if not top or item[key] > top[key]:
            top = item
    return top

students = [
    {'name': '张伟', 'score': 85},
    {'name': '刘洋', 'score': 95},
    {'name': '陈静', 'score': 88},
]
print(top_by(students, 'score'))