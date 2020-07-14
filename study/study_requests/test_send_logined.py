from requests import session

"""
请求需要登录后的接口（需鉴权）：
使用session对象发送请求(session对象发送请求可记录上一次请求的cookies信息)

"""
s = session()
# 准备登录接口数据
url_login = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
params_login = {
    'mobilephone': '13133333333',
    'pwd': '123456'
}
# 请求登录接口
response_login = s.post(url=url_login, data=params_login)
# 获取响应
print(response_login.json())


# 准备数据
url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
params = {
    'mobilephone': '13133333333',
    'amount': 100
}

# 请求接口
response = s.post(url=url, data=params)

# 获取响应
print(response.json())