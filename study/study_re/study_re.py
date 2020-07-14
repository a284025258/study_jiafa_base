import re
"""
正则表达式
"""
# match 查找 从字符串头部开始匹配（目标字符串必须在开头位置），如果匹配到了，返回匹配的对象
# findall 把所有符合规则的都匹配出来，返回列表
# search 查找 在整个字符串中进行匹配，如果匹配到了，返回匹配的对象（只会匹配符合规则的第1个）

# sub 替换

str1 = '123python456python'
# \d 匹配数字 \D 匹配非数字 \w 匹配单词字符[a-z,A-Z,0-9,下划线] \W 匹配非字母 {m} 匹配 m 次 {m.} 至少匹配 m 次  . 匹配任意1个字符（除\n） + 匹配一次以上
# * 匹配0次以上 ^string 匹配以某字符串开头(sting必须在开头处) $sting 匹配以某字符串结尾(string必须在结尾处)   ? 关闭贪婪模式
# print(re.search(r'\d', str1))
str2 = '{"mobilephone": "#phone#", "pwd": "#pwd#", "regname": "#regname#"}'

res = re.search(r'#(.+?)#', str2)
# print(res)
# print(res.group(1))
#
# print(re.findall('python', str1))
# print(re.search(r'[p6]', str1))
str3 = "python123python456python"
print(re.findall(r'py(th)on$', str3))