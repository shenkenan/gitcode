import time

f = open("E:/word11.txt", "w" , encoding = "UTF-8")
f.write("hello 黑马程序员!!!")
print(f"{f}")
f.flush()
# time.sleep(500000)
f.close()