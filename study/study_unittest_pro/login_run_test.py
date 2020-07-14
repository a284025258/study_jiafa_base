import unittest
import test_login
# from study_excel.read_excel import ReadExcel
from study_excel_plus.read_excel import ReadExcel
from HTMLTestRunner import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例添加到测试套件
# 方法一：
# addTest 添加单条测试用例
# 批量添加入参及预期结果
# cases = [{'expect': {'code': 0, 'msg': '登录成功'}, 'data': {'username': 'admin','password': '123456'}, 'method': 'test01_login_case_pass'},
#          {'expect': {'code': 0, 'msg': '登录成功'}, 'data': {'username': 'admin','password': '123456'}, 'method': 'test01_login_case_pass'},
#          {'expect': {'code': 0, 'msg': '登录成功'}, 'data': {'username': 'admin','password': '123456'}, 'method': 'test01_login_case_pass'},
#          {'expect': {'code': 0, 'msg': '登录成功'}, 'data': {'username': 'admin','password': '1234567'}, 'method': 'test01_login_case_pass'}]
read_excel = ReadExcel('../study_excel/cases.xlsx', 'login')
# 直接读取Excel表格数据
# cases = read_excel.read_data()
# for case in cases:
#     suite.addTest(login_test.LoginTestCase(case['expect'], case['data'], case['method']))
# 将Excel表头与每行数据封装成一个对象来读取数据
cases = read_excel.read_data_obj()
for case in cases:
    suite.addTest(test_login.LoginTestCase(case.expect, case.data, case.method))

# 方法二：
# loader 加载1个测试用例类的所有测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(login_test.LoginTestCase))

# 方法三：
# 添加1个模块内的所有测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(login_test))

# 方式四：
# 添加1个路径下的所有测试用例
# loader = unittest.TestLoader()
# 此处匹配文件名以“test”开头的“.py”类型的文件
# suite.addTest(loader.discover(r'D:\PycharmProjects\untitled\venv\study\study_unittest'))

# 创建测试用例运行程序
# runner = unittest.TextTestRunner()
# runner.run(suite)

# HTMLTestRunner
with open('report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb, title='测试报告', description='日常发布测试')
    runner.run(suite)