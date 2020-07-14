import unittest
import login_test
from HTMLTestRunner import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 将测试用例添加到测试套件
# 方法一：
# addTest 添加单条测试用例
# suite.addTest(login_test.LoginTestCase('test01_login_case_pass'))

# 方法二：
# loader 加载1个测试用例类的所有测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(login_test.LoginTestCase))

# 方法三：
# 添加1个模块内的所有测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(login_test))

# 方式四：（有问题）
# 添加1个路径下的所有测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r'D:\PycharmProjects\untitled\venv\study\study_unittest'))

# 创建测试用例运行程序
# runner = unittest.TextTestRunner()
# runner.run(suite)

# HTMLTestRunner
with open('report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb, title='测试报告', description='日常发布测试')
    runner.run(suite)