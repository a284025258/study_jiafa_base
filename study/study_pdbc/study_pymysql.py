import pymysql


# 连接到数据库
conn = pymysql.connect(host="test.lemonban.com", user="test", password="test", database="future", port=3306,)
# 创建游标
cur = conn.cursor()
# 执行sql语句
sql = "SELECT * FROM member LIMIT 0, 5"
# 获取结果
cur.execute(sql)
result = cur.fetchall()
for i in result:
    print(i)
# 增删改，需提交事务
# conn.commit()
