import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts, LegendOpts, TooltipOpts, LabelOpts

# 处理数据
# 美国的全部内容
f_us = open("D:/python-learn/python图表数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
# 日本的全部内容
f_jp = open("D:/python-learn/python图表数据/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
# 印度的全部内容
f_in = open("D:/python-learn/python图表数据/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

# 美国疫情数据处理
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
# JSON转python字典
us_dict = json.loads(us_data)
# 获取trend key
us_trend_data = us_dict["data"][0]["trend"]
# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data["updateDate"][:314]
# 获取确认数据，用于y轴，取2020年（到315下标结束）
us_y_data = us_trend_data["list"][0]["data"][:314]


#日本疫情数据处理
# 去掉不合JSON规范的开头
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
# 去掉不合JSON规范的结尾
jp_data = jp_data[:-2]
# JSON转python字典
jp_dict = json.loads(jp_data)
# 获取日期数据，用于x轴，取2020年（到314下标结束）
jp_x_data = jp_dict["data"][0]["trend"]["updateDate"][:314]
# 获取确诊数据，用于y轴，取2020年（到314下标结束）
jp_y_data = jp_dict["data"][0]["trend"]["list"][0]["data"][:314]

#印度疫情数据处理
# 去掉不合JSON规范的开头
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 去掉不合JSON规范的结尾
in_data = in_data[:-2]
# JSON转python字典
in_dict = json.loads(in_data)
# 获取日期数据，用于x轴，取2020年（到314下标结束）
in_x_data = in_dict["data"][0]["trend"]["updateDate"]
# 获取确诊数据，用于y轴，取2020年（到314下标结束）
in_y_data =in_dict["data"][0]["trend"]["list"][0]["data"]


#生成折线图

#得到折线图对象
line = Line()
#添加X轴数据,X轴数据通用，只需要添加一份
line.add_xaxis(us_x_data)
#添加Y轴数据，数据不共用，需要添加3个Y轴数据
line.add_yaxis("美国疫情确诊", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本疫情确诊", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度疫情确诊", in_y_data, label_opts=LabelOpts(is_show=False))

#全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="全球疫情数据",pos_left="center",pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)
)
#生成图表
line.render()
# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()