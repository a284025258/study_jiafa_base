import pymysql


class MyPDBC:
    # 连接数据库
    def connect_db(self, hostname='localhost', username='root', password='123456', database='python_study', port=3306):
        connect = pymysql.connect(hostname, username, password, database, port)
        return connect

    # 查询
    def search_db(self, sql):
        connect = self.connect_db()
        cursor = connect.cursor()  # 获取游标
        cursor.execute(sql)  # 执行语句
        result = cursor.fetchall()  # 获取执行结果
        connect.close()  # 关闭数据库
        return result

    # 增删改
    def fix_db(self, sql):
        connect = self.connect_db()
        cursor = connect.cursor()  # 获取游标
        cursor.execute(sql)  # 执行语句
        connect.commit()  # 提交数据库
        connect.close()  # 关闭数据库


if __name__ == "__main__":
    myPDBC = MyPDBC()
    result = myPDBC.search_db('SHOW DATABASES')
    # myPDBC.fix_db('INSERT INTO userinfo(username,password,telephone) VALUES("888888","123456","13423211212")')
    print(result)
