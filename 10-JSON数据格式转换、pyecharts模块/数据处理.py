import json

# 处理数据
f_us = open("D:/python-learn/python练习/美国.txt", "r", encoding="UTF-8")
# 美国的全部内容
us_data = f_us.read()
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
# JSON转python字典
us_dict = json.loads(us_data)
print(type(us_dict))
print(us_dict)
# 获取trend key
trend_data = us_dict["data"][0]["trend"]
print(trend_data)
#