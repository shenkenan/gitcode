import time

# f = open("E:/测试.txt", "r" , encoding = "UTF-8")
# print(type(f))

# test = f.read()
# print(f"{test}")
# content = f.readlines()
# print(f"{content}")
# print(type(content))

# for line in f:
#     print(f"{line}")
# time.sleep(500000)

# f.close()
# with open("E:/测试.txt", "r" , encoding = "UTF-8") as f:
#     for line in f:
#         print(f"{line}")

f = open("E:/word.txt", "r", encoding = "UTF-8")
test = f.read()
tongji = test.count("itheima")
# tongji = 0
# for i in test:
#     test.count("itheima")
#     tongji += 1
print(f"itheima出现次数为：{tongji}")

f.close()