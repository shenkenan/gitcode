import random

yue = 10000
fafang = 1000
for i in range(1,21):
    import random
    jixiao = random.randint(1,10)

    if jixiao < 5:
        print(f"员工{i}绩效分是{jixiao}低于5分，不发工资，下一位。")
        continue

    else:
        yue = yue - fafang
        if yue == 0:
            print(f"账户余额还剩余{yue}元，本月工资发完了，请下个月领取。")
            break
        else:
            print(f"向员工{i}发放{fafang}元，账户余额还剩{yue}元")