# def list_while_func():
#     my_list = ["传智教育","黑马程序员","python"]
#     index = 0
#     while index < len(my_list):
#         element = my_list[index]
#         print(f"列表的元素：{element}")
#         index += 1
#
#
# def list_for_func():
#     my_list = [1,2,3,4,5,6,7,8,9]
#     for i in my_list:
#         print(f"列表的元素有：{i}")
#
# list_while_func()
# list_for_func()


def list_for_func():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k_list = []
    for num in mylist:
        if num %2 == 0:
            k_list.append(num)
    print(f"{k_list}")



def list_while_func():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k_list = []
    index = 0
    while index < len(mylist):
        element = mylist[index]
        if element %2 == 0:
            k_list.append(element)
        index +=1
    print(f"{k_list}")



list_for_func()
list_while_func()