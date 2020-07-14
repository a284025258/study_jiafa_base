import requests

# 第一步：准备请求数据
url = 'https://wwww.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
params = {'wd': '拉勾'}
# 第二步：发送请求： get请求
response = requests.get(url=url, headers=headers, params=params)
# 第三步：获取响应结果
# 1.自动识别编码方式，对内容进行解码
# print(response.text)
# 2.指定编码方式
print(response.content.decode('utf8'))
