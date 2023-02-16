
import random
num = random.randint(1,100)
wuxian = True
jishu = 0

while wuxian:
    git_num = int(input("请输入你猜测的数字！"))
    jishu = jishu+1
    if git_num == num:
        print("恭喜你，猜中了！")
        wuxian = False
    else:
        if git_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")

print(f"你一共猜测了{jishu}次。")