class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def jiao(Animal):
    Animal.speak()

dog = Dog()
cat = Cat()

jiao(dog)
jiao(cat)

# 抽象类

class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

class meidi_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print("美的空调摆风")

class geli_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print("格力空调摆风")

def kongtiao(AC):
    AC.cool_wind()
    AC.hot_wind()



meidi_ac = meidi_AC()
geli_ac = geli_AC()

kongtiao(meidi_ac)
kongtiao(geli_ac)
