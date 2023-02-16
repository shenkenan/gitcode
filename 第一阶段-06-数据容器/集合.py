# my_set = {"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
# my_set_emp = set()
# print(f"{my_set}")
#
# my_set.add("python")
# my_set.add("传智教育")
# print(f"{my_set}")
# my_set.remove("黑马程序员")
# print(f"{my_set}")

# set1 = {1,2,3}
# set2 = {1,5,6}
# re1 = set1.difference(set2)
# print(re1)
# print(set1)
# print(set2)

# set1 = {1,2,3}
# set2 = {1,5,6}
# set1.difference_update(set2)
# print(set1)
# print(set2)
# set3 = set1.union(set2)
# print(set3)
# num = len(set3)
# print(num)

# for i in set3:
#     print(f"{i}")


my_list = ["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast"]
jihe = set(my_list)
for i in my_list:
    jihe.add(i)
print(f"{jihe}")