import requests

# r = requests.get("https://static1.scrape.cuiqingcai.com/")
param = {
    'name': 'Tom',
    'age': 25
}
r = requests.get("http://httpbin.org/get", params=param)
print(r.text)
print(r.json())
