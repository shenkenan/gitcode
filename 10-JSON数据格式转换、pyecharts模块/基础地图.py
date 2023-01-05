from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()
# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 1299),
    ("湖南省", 399),
    ("台湾省", 499),
    ("安徽省", 599),
    ("广东省", 899),
    ("河南省", 9),
]
# 添加数据
map.add("地图", data, "china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "laber": "1-9", "color": "#9b53ed"},
            {"min": 10, "max": 99, "laber": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 1000, "laber": "100-1000", "color": "#990033"}
        ]
    )
)



# 绘图
map.render()
