import unittest
from login import login_check

class LoginTestCase(unittest.TestCase):
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

    '''登录测试用例'''
    def test01_login_case_pass(self):
        '''正常登录'''
        # 准备测试用例数据 1.入参 2.预期结果
        username = 'admin'
        password = '1234567'
        expect = {'code': 0, 'msg': '登录成功'}
        # 执行功能函数，获取实际结果
        result = login_check(username, password)
        # 断言预期和实际结果
        try:
            self.assertEqual(expect, result)
        except AssertionError as e:
            print('该条用例未通过')
            print(f'预期结果：{expect}')
            print(f'实际结果：{result}')
            raise e
        else:
            print('该条用例通过')
            print(f'预期结果：{expect}')
            print(f'实际结果：{result}')
    def test02_login_case_pwd_error(self):
        pass