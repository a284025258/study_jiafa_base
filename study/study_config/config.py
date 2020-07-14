from configparser import ConfigParser

# 创建一个配置解析器对象
conf = ConfigParser()
conf.read('config.ini', encoding='utf8')
host = conf.get('mysql', 'host')
print(host)
# 获取所有配置项
sections = conf.sections()
# print(sections)
# 获取单个配置项下所有配置内容 name
mysql_options = conf.options('mysql')
# print(mysql_options)
# 获取单个配置项下所有配置内容 name&value
mysql_items = conf.items('mysql')
print(mysql_items)

# 写入配置项
# 判断配置项是否存在
if not conf.has_section('test'):
    conf.add_section('test')
# 写入配置内容
conf.set('test', 'name', 'Jax')
with open(file='config.ini', mode='w', encoding='utf8') as fp:
    conf.write(fp)
