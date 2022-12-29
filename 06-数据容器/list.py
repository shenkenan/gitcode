# my_list = ["itheima","itcast",666,888,666,[1,2,3,4,],[8,9,10,11]]
# # print(my_list)
# # print(type(my_list))
# # print(my_list[-1][3])
# # index = my_list.index(666)
# # print(f"666黑马在列表中的下表索引值是：{index}")
#
# # my_list[0] = "传智播客"
# # print(f"列表呗修改元素值后，结果是：{my_list}")
# # my_list[-2][1] = "黑马程序员"
# # print(f"列表呗修改元素值后，结果是：{my_list}")
# #
# # my_list.insert(-1,"传智黑马")
# # print(f"列表呗修改元素值后，结果是：{my_list}")
#
# # my_list.append("我是高级程序员")
# # print(f"列表呗修改元素值后，结果是：{my_list}")
#
# # my_list2 = [50,10,26,30]
# # my_list.extend(my_list2)
# # print(f"列表呗修改元素值后，结果是：{my_list}")
#
# # del my_list[-1]
# # print(f"列表呗修改元素值后，结果是：{my_list}")
#
# # my_list.pop(-1)
# # print(f"列表呗修改元素值后，结果是：{my_list}")
#
# # my_list.remove("itcast")
# # print(f"列表呗修改元素值后，结果是：{my_list}")
#
# # my_list.clear()
# # print(f"列表呗修改元素值后，结果是：{my_list}")
# # count = my_list.count(666)
# # print(f"列表呗修改元素值后，结果是：{count}")
#
# count = len(my_list)
# print(count)

mylist = [21,25,21,23,22,20]
mylist.append(31)
mylist.extend([29,33,30])
num1 = mylist[0]
num2 = mylist[-1]
print(f"{mylist}")
print(f"{num1}")
print(f"{num2}")

index = mylist.index(31)
print(f"{index}")
print(f"{mylist}")