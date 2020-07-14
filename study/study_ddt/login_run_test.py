import unittest
from HTMLTestRunner import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 加载测试用例套件
loader = unittest.TestLoader()
# 此处匹配文件名以“test”开头的“.py”类型的文件
suite.addTest(loader.discover(r'D:\PycharmProjects\lemon\study\study_ddt'))

# HTMLTestRunner 生成测试报告
with open('report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb, title='测试报告', description='日常发布测试')
    runner.run(suite)
