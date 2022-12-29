def user_info(name, age ,gender = "男"):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")

user_info("小明",20,"男")
user_info(name="小紫", age=18, gender="女")
user_info(age=18, gender="女", name="小紫")
user_info("小紫", 18, gender="女")
user_info("小王", 19)


def user_info(*args):
    print(args)

user_info(1,2,3,"小名","男")

def user_info(**kwargs):
    print(kwargs)

user_info(name = "小白", age = 18)