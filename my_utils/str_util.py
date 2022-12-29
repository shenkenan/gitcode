def str_reverse(s):#接受传入字符串，将字符串反转返回
    for i in s:
        my_str = i[-1]
        print(my_str)


def substr(s, x, y):#按照下标x和y，对字符串进行切片
    s_split = s.split(x, y)
    print(s_split)

str_reverse()
substr()