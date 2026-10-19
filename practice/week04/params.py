def greet (name,greeting='你好'):
    print(f"{greeting},{name}")

greet("胡乐轩")
greet("胡乐轩",greeting="Hi")
greet("胡乐轩","Hi")

def add_item(item, bag=[]):
    bag.append(item)
    return bag

print(add_item("苹果"))
print(add_item("香蕉"))