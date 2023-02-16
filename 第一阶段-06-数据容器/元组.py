# t1 = (1,2,3,4,5,"heima")
# t2 = ()
# t3 = tuple()
# t4 = ("hello",)
# print(f"{type(t1)}")
# print(f"{t2}")
# print(f"{t3}")
# print(f"{type(t4)}")
#
# t5 = ((1,2,3,),(4,5,6,))
# print(f"{type(t5)},内容是：{t5}")
#
# tt = t5[1][-1]
# print(f"{tt}")
#
# index =t1.index(4)
# print(f"{index}")

yuanzu = ("周杰伦",11,["football","music"])

index = yuanzu.index(11)
name = yuanzu[0]
print(f"{index}")
print(f"{name}")
del yuanzu[2][0]
print(f"{yuanzu}")

yuanzu[2].append("coding")
print(f"{yuanzu}")