import unittest
from study.project.common.my_logger import log
from study.project.common.HTMLTestRunner import HTMLTestRunner
from study.project.common.constant import CASES_DIR, REPORTS_DIR
import os

log.info('---------------------------------------测试开始---------------------------------------')
# 创建测试套件
suite = unittest.TestSuite()

# 加载测试用例套件
loader = unittest.TestLoader()
# 此处匹配文件名以“test”开头的“.py”类型的文件
suite.addTest(loader.discover(CASES_DIR))

# HTMLTestRunner 生成测试报告
with open(file=os.path.join(REPORTS_DIR, 'report.html'), mode='wb') as fb:
    runner = HTMLTestRunner(stream=fb, title='测试报告', description='日常发布测试', tester='石高林')
    runner.run(suite)
log.info('---------------------------------------测试结束---------------------------------------')
