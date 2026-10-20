# try:
#     f=open('不存在的文件.json','r')
# except FileNotFoundError:
#     print("文件不存在，我来创建一个")
#     f=open("不存在的文件.json",'w')
#
# print("程序还活着，继续往下跑")

nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)