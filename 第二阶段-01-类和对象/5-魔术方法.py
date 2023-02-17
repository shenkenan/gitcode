class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # __str__ 魔术方法
    def __str__(self):
        return f"student类对象，name:{self.name},age:{self.age}"

stu = student("周杰伦", 33)
print(stu)
print(str(stu))

# __str__ 魔术方法