# 定义一个带有成员方法的类
class student:
    name = None       # 学生姓名

    def say_hi(self):
        print(f"大家好呀，我是{self.name}，欢迎大家多读关照")


    def say_hi2(self,msc):
        print(f"大家好呀，我是{self.name},{msc}")

stu = student()
stu.name = "林俊杰"
stu.say_hi2("哎哟啊，大家好啊")

stu2 = student()
stu2.name = "周杰伦"
stu2.say_hi2("哈哈，幸会幸会")