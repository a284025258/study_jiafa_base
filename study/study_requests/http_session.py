from requests import session
class HttpSession(object):
    s = session()

    def __init__(self, url_login, url_business, data_login, data_business, method):
        self.url_login = url_login
        self.url_business = url_business
        self.data_login = data_login
        self.data_business = data_business
        self.method = method
    def login(self):
        response = self.s.post(url=self.url_login, data=self.data_login)
    def send(self):
        if 'get' == self.method:
            response = self.s.get(url=self.url_business, params=self.data_business)
            return response.text
        elif 'post' == self.method:
            response = self.s.post(url=self.url_business, data=self.data_business)
            return response.text


if __name__ == '__main__':
    url_login = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    data_login = {
        'mobilephone': '13133333333',
        'pwd': '123456'
    }
    url_business = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    data_business = {
        'mobilephone': '13133333333',
        'amount': 100
    }
    http_session = HttpSession(url_login=url_login, url_business=url_business, data_login=data_login, data_business=data_business, method='post')
    http_session.login()
    response = http_session.send()
    print(response)