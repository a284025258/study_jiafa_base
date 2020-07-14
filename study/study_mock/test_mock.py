from unittest import mock

"""
mock的用法
"""
url = "https://openapi.alipay.com/getway.do"
data = {"user": "Jax"}
request = mock.Mock(return_value='{"code": 1, "msg": "支付成功"}')
print(request(url, data))