# 设计一个闹钟类
class clock:
    id = None          # 序列号
    price = None       # 价格



    def rinng(self):
        import  winsound

        winsound.Beep(2000, 3000)
# 构建2个闹钟对象并让其工作

clock1 = clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID：{clock1.id},价格：{clock1.price}")
clock1.rinng()

clock2 = clock()
clock2.id = "003033"
clock2.price = 91.99
print(f"闹钟ID：{clock2.id},价格：{clock2.price}")
clock2.rinng()