# age = 10
# print(f"我已经{age}岁了！")
# if age >= 18:
#     print("我已经成年了")
#     print("即将步入大学生活")
# print(f"时间过的真快啊")
#
# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄："))
# #age = int(age)
# if age >= 18:
#     print(f"您的年龄是{age}岁，您已成年，游玩需要补票10元。")
# else:
#     print(f"您的年龄是{age}岁，您还未成年，游玩不需要补票。")
# print("祝您游玩愉快！！！")
#
# print("欢迎来到黑马动物园。")
# biaozhun = int(input("请输入可以免费游玩的身高。"))
# shengao = int(input("请输入你的身高（cm）。"))
#
# if shengao >= biaozhun:
#     print(f"您的身高是：{shengao}cm,超过了{biaozhun}cm，游玩需要补票10元。")
# else:
#     print(f"您的身高是：{shengao}cm，未超过{biaozhun}cm，您可以免费游玩。")
# print("祝您游玩愉快！")


# num = int(input("请输入你的心里数字。"))
# if num == int(input("请输入你第一次猜想的数字。")):
#     print("恭喜你猜对了！")
# elif num == int(input("不对，再猜一次。")):
#     print("恭喜你猜对了！")
# elif num == int(input("不对，再猜最后一次。")):
#     print("恭喜你猜对了！")
# else:
#     print(f"sorry,全部猜错了，我想的是：{num}。")

import random
num = random.randint(1,10)

cai_num = int(input("请输入你要猜的数字。"))
if cai_num == num:
    print("恭喜你，第一次就猜对了。")
else:
    if cai_num > num:
        print("你猜的大了。")
    else:
        print("你猜的小了。")
    cai_num = int(input("请输入你要猜的数字。"))
    if cai_num == num:
        print("恭喜你，第二次猜中了。")
    else:
        if cai_num > num:
            print("你猜的大了。")
        else:
            print("你猜的小了。")
        cai_num = int(input("请输入你要猜的数字。"))
        if cai_num == num:
            print("恭喜你，你最后一次猜对了。")
        else:
            if cai_num > num:
                print("你猜的大了。")
                print("这个幸运数字是：%d" % num)
            else:
                print("你猜的小了。")
                print("这个幸运数字是：%d"%num)

