from pymysql import Connection

# 获取到mysql数据库的链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="2+2=2error"
)

# print(conn.get_server_info())
# 执行非查询性质语句
cursor = conn.cursor()
conn.select_db("world")
# 使用游标对象，执行sql语句

# cursor.execute("create table test_pymysql(id int)")
# 执行查询性质的sql语句
cursor.execute("select * from student")

results = cursor.fetchall()

for r in results:
    print(r)
# 关闭数据库的链接
conn.close()