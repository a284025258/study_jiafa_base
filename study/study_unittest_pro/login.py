
def login_check(username, password):
    '''
    登录函数
    :param username:
    :param password:
    :return:
    '''
    if 6 <= len(password) <= 18:
        if username == 'admin' and password == '123456':
            return {'code': 0, 'msg': '登录成功'}
        else:
            return {'code': 1, 'msg': '帐号或密码不正确'}
    else:
        return {'code': 1, 'msg': '密码长度在6-18位之间'}