from suds import client
"""
webservice的用法
"""

url = 'webservice url'
data = '{"args_name": "args_value"}'
c = client.Client(url)
# sendMCode 接口名
c.service.sendMCode(data)