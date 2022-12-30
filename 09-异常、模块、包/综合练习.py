import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马次哼许愿"))
print(my_utils.str_util.substr("itheima", 0, 4))


file_util.append_to_file("E:test111.txt", "itheima")
file_util.print_file_info("E:/test111.txt")