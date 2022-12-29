# zidian = {"张三":99,"李四":88,"王五":77}
# print(f"{zidian}")
# zidian2 = {}
# zidian3 = dict()
# print(f"{type(zidian)}")
# zidian = {"张三":99,"李四":88,"王五":77}
# mystr = zidian["李四"]
# print(f"{mystr}")

# zidian = {
#     "王力宏":{"语文":77,"数学":66,"英语":33},
#     "周杰伦":{"语文":88,"数学":86,"英语":55},
#     "张学友":{"语文":99,"数学":96,"英语":66}
# }
# mystr = zidian["周杰伦"]["语文"]
# mystr1 = zidian["张学友"]["英语"]
# print(f"{mystr}")
# print(f"{mystr1}")
# zidian["吴亦凡"] = "语文"
# zidian["吴亦凡"] = "数学"
# zidian["吴亦凡"] = "英语"
# zidian.pop("周杰伦")
# zidian.clear()

# for i in zidian:
#     zidian1 = zidian.keys()
#     mystr = zidian[i]
#     print(f"{zidian1}")
#     print(f"{mystr}")

xinxi = {
    "王力宏":{"部门":"科技部","工资":3000,"级别":1},
    "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
    "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
    "张学友":{"部门":"科技部","工资":4000,"级别":1},
    "刘德华":{"部门":"市场部","工资":6000,"级别":2}
}
print(f"全体员工当前信息如下：{xinxi}")
# my_zidian = xinxi.keys()
# # print(f"{my_zidian}")
# for i in my_zidian:
#     if xinxi[i]["级别"] == 1:
#         xinxi[i]["级别"] += 1
#         xinxi[i]["工资"] += 1000
# print(f"全体员工级别为1的员工完成升职加薪操作，操作后：{xinxi}")

for name in xinxi:
    if xinxi[name]["级别"] == 1:
        xinxi[name]["级别"] += 1
        xinxi[name]["工资"] += 1000

        # gerenxinxi = xinxi[name]
        # gerenxinxi["级别"] += 1
        # gerenxinxi["工资"] += 1000
        # xinxi[name] = gerenxinxi
print(f"全体员工级别为1的员工完成升职加薪操作，操作后：{xinxi}")