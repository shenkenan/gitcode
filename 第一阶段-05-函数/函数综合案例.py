money = 5000000
name = str(input("请输入您的姓名！"))

def zhucd():
    """
    主菜单，选择相应按键进入到相应的需求函数
    :return:
    """
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额{输入1}")
    print("存款{输入2}")
    print("取款输入{3}")
    print("退出输入{4}")
    anjian = int(input("请输入您的选择："))
    while True:
        if anjian == 1:
            chaxun()
            continue
        elif anjian == 2:
            cunkuan()
            continue
        elif anjian == 3:
            qukuan()
            continue
        else:
            break

def chaxun():
    print("------查询余额------")
    print(f"{name},您好，您的余额剩余：{money}元")

def cunkuan():
    print("------存款------")
    jine = int(input("请输入您要存款的金额！"))
    global money
    money = money + jine
    print(f"{name}，您好，您存款{jine}元成功")
    print(f"{name}，您好，您的余额剩余:{money}元")
def qukuan():
    print("------取款------")
    jine = int(input("请输入您要取款的金额！"))
    global money
    money = money - jine
    print(f"{name}，您好，您取款{jine}元成功")
    print(f"{name}，您好，您的余额剩余：{money}元")

zhucd()