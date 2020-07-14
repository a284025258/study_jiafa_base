import unittest
from study.project.lib.ddt import ddt, data
from study.project.common.read_excel import ReadExcel
from study.project.common.http_requests import HttpRequest
from study.project.common.my_logger import log
import os
from study.project.common.constant import DATA_DIR

@ddt
class LoginTestCase(unittest.TestCase):
    read_excel = ReadExcel(os.path.join(DATA_DIR, 'cases.xlsx'), 'login')
    # 通过字典获取数据
    # cases = read_excel.read_data()
    # 通过对象获取数据
    cases = read_excel.read_data_obj()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    '''@data读取数据，有多少条数据，生成多少条测试用例'''
    @data(*cases)
    def test_login_case(self, case):
        """登录接口测试用例"""
        # 准备测试用例数据
        method = case.method
        url = case.url
        expected = eval(case.expected)
        param = eval(case.param)
        # 发送请求接口，获取结果
        log.info(f'正在请求地址：{url}')
        http_request = HttpRequest()
        response = http_request.request(url=url, method=method, data=param)
        result = response.json()
        # 断言预期和实际结果
        row = case.case_id + 1
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            print('该用例执行未通过')
            self.read_excel.write_data(row=row, column=8, value='未通过')
            print(f'预期结果：{expected}')
            print(f'实际结果：{result}')
            log.error(e)
            log.info('[{case.title}] --> 该用例执行未通过')
            raise e
        else:
            print('该用例执行通过')
            self.read_excel.write_data(row=row, column=8, value='通过')
            print(f'预期结果：{expected}')
            print(f'实际结果：{result}')
            log.info(f'[{case.title}] --> 该用例执行通过')