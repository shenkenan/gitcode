# def say_hi():
#     print("你好啊！！！")
# say_hi()

# def hesuan():
#     print("欢迎来到黑马程序员！")
#     print("请初始您的健康码以及72小时核算证明！")
#
# hesuan()

# def add(x, y):
#     result = x + y
#     print(f"{x} + {y}的计算结果是：{result}")
#
# add(3, 6)
# add(105, 875)

# def celiang(x):
#     print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
#     tiwen = int(input("体温测量中，您的体温是："))
#     if tiwen < 37.5:
#         print(f"您的体温是：{tiwen},体温正常，请进入！")
#
#     else:
#         print(f"您的体温是：{tiwen},体温异常，需要隔离！")
#
# celiang()

# def celiang(x):
#     print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
#     if x < 37.5:
#         print(f"您的体温是：{x},体温正常，请进入！")
#     else:
#         print(f"您的体温是：{x},体温异常，需要隔离！")
#
# celiang(37.2)

# def add(a, b):
#     """
#     两数相加
#     :param a:其中一个形参
#     :param b: 另外一个形参
#     :return: 返回两数相加之和
#     """
#     result = a + b
#     return result
# add(52, 85)

def func_b():
    print("---2---")

def func_a():
    print("---1---")
    func_b()
    print("---3---")

func_a()