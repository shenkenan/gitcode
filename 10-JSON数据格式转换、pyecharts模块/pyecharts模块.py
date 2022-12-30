from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
#给折线图对象添加X，Y轴的数据
line.add_xaxis(["秦国","楚国","燕国","齐国","赵国","魏国","韩国"])
line.add_yaxis("GDP",[80,70,60,40,50,10,30,20])


#设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title = "GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)


)

#生成图表
line.render()