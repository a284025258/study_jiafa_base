import requests

# 准备请求数据
url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
data = {
    'mobilephone': '13133333334',
    'pwd': '123456',
    'regname': 'Jax'
}
# 发送请求 data参数接收传入参数
response = requests.post(url=url, data=data)
# 获取响应内容
print(response.text)
# post请求独有获取响应内容：json()，只有返回内容为json格式才可接收
# json()方法可以将返回的json格式字符串，转换为python对应的字典或列表格式
print(response.json())