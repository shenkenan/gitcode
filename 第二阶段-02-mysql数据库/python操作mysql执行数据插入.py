from pymysql import Connection


conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="2+2=2error",
    autocommit=True
)

# 执行非查询性质sql
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 执行sql
cursor.execute("insert into student values(10023,'花百岁',18,'女')")
# 手动确认
conn.commit()
# 关闭连接
conn.close()