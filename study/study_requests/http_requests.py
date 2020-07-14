import requests


class HttpRequest(object):
    """直接发送请求不记录cookies"""
    def request(self, url, method, data=None, headers=None):
        method = method.lower()
        if method == 'get':
            return requests.get(url=url, params=data, headers=headers)
        elif method == 'post':
            return requests.post(url=url, data=data, headers=headers)

class HttpSession(object):
    """发送请求并记录cookies"""
    def __init__(self):
        self.session = requests.session()

    def request(self, url, method, data=None, headers=None, json= None):
        method = method.lower()
        if method == 'get':
            return self.session.get(url=url, params=data, headers=headers, json=json)
        elif method == 'post':
            return self.session.post(url=url, data=data, headers=headers, json=json)

    def close(self):
        self.session.close()

# if __name__ == '__main__':
#     # url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
#     # data = {
#     #     'mobilephone': '13133333334',
#     #     'pwd': '123456',
#     #     'regname': 'Jax'
#     # }
#     # hr = HttpRequest()
#     # response = hr.request(url=url, method='POST', data=data)
#     # print(response.json())
#     url_login = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
#     data_login = {
#         'mobilephone': '13133333333',
#         'pwd': '123456'
#     }
#     url_business = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
#     data_business = {
#         'mobilephone': '13133333333',
#         'amount': 100
#     }
#     hs = HttpSession()
#     hs.request(url=url_login, method='post', data=data_login)
#     response = hs.request(url=url_business, method='Post', data=data_business)
#     print(response.json())