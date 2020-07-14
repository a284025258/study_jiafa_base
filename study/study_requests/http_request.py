import requests


class HttpRequest(object):
    def __init__(self, url, params, method):
        self.url = url
        self.params = params
        self.method = method

    def send(self):
        if 'get' == self.method:
            response = requests.get(url=self.url, params=self.params)
            return response.text
        elif 'post' == self.method:
            response = requests.post(url=self.url, data=self.params)
            return response.text


if __name__ == '__main__':
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
    data = {
        'mobilephone': '13133333334',
        'pwd': '123456',
        'regname': 'Jax'
    }
    http_request = HttpRequest(url=url, params=data, method='post')
    response = http_request.send()
    print(response)