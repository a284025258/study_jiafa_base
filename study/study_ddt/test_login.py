import unittest
from login import login_check
from ddt import ddt, data
from study.study_excel_plus.read_excel import ReadExcel


@ddt
class LoginTestCase(unittest.TestCase):
    read_excel = ReadExcel('../study_excel/cases.xlsx', 'login')
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
    def test01_login_case_pass(self, case):
        """
        正常登录
        :param case: cases拆包后的集合
        :return:
        """
        # 通过字典获取数据
        # expect = eval(case['expect'])
        # data = eval(case['data'])
        # 通过对象获取数据
        expect = eval(case.expect)
        data = eval(case.data)
        result = login_check(**data)
        # 断言预期和实际结果
        try:
            self.assertEqual(expect, result)
        except AssertionError as e:
            print('该条用例未通过')
            self.read_excel.write_data(row=case.case_id+1, column=5, value='未通过')
            print(f'预期结果：{case.expect}')
            print(f'实际结果：{result}')
            raise e
        else:
            print('该条用例通过')
            self.read_excel.write_data(row=case.case_id+1, column=5, value='通过')
            print(f'预期结果：{case.expect}')
            print(f'实际结果：{result}')
    def test02_login_case_pwd_error(self):
        pass

