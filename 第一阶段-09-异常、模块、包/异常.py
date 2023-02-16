#捕获基础异常

# f = open("E:/test", "r", encoding = "UTF-8")

# try:
#     f = open("E:/test.txt", "r", encoding="UTF-8")
# except:
#     f = open("E:/test.txt", "w", encoding="UTF-8")

#捕获指定异常
# try:
#     print(name)
#
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)

#捕获多个异常

# try:
#     1/0
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义的异常 或者 除以0的异常错误")

def func1():
    print("func1 开始执行")
    num = 1 / 0
    print("func1 结束执行")

def func2():
    print("func2开始执行")
    func1()
    print("func2执行结束")

# def main():
#         func2()

def main():
    try:
        func2()
    except Exception as e:
        print("出现异常了")
        print(f"{e}")

main()