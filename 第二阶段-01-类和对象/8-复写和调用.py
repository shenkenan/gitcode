class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5G(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITheima"

    def call_by_5G(self):
        print("开启CPU单核模式，确保童话的时候省电")
        print(f"父类的厂商是{Phone.producer}")
        super().call_by_5G()
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
print(phone.producer)
phone.call_by_5G()

# 在子类中，调用父类成员



