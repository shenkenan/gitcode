# my_str = "itheima and itcast"
#
# value = my_str[2]
# print(f"{value}")


# my_str = "   12itheima and itcast21   "
# now_list= my_str.split(" ")
# print(f"{now_list}")
#
# new_str = my_str.strip("12")
# print(f"{my_str},{new_str}")

# my_str = "黑马程序员"
# index = 0
# while index < len(my_str):
#     print(my_str[index])
#     index +=1

# my_str = "黑马程序员"
# for i in my_str:
#     print(f"{i}")

my_str = "itheima itcast boxuegu"
count = my_str.count("it")
tihuan = my_str.replace(" ", "|")
fenge =tihuan.split("|")
print(f"字符串{my_str}中有：{count}个it字符")
print(f"字符串{my_str}，呗替换空格后，结果：{tihuan}")
print(f"字符串{tihuan}，按照|分隔后，得到：{fenge}")