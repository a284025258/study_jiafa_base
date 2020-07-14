import logging


"""
调试方法一：print大法
调试方法二：断点调试
调试方法三：日志调试
"""
# 创建日志收集器
mylog = logging.getLogger('mylog')

# 设置日志收集器，收集的日志等级
mylog.setLevel(logging.DEBUG)

# 创建输出渠道：1.输出到控制台
sh = logging.StreamHandler()

# 设置输出渠道收集日志等级
sh.setLevel(logging.DEBUG)

# 创建输出渠道：2.输出到文件
fh = logging.FileHandler(filename='./mylog.log', mode='a', encoding='utf8')
fh.setLevel(logging.WARNING)

# 将输出渠道添加到日志收集器
mylog.addHandler(sh)
mylog.addHandler(fh)

# 设置日志格式
format = '[%(asctime)s] - [%(filename)s --> line:%(lineno)d] - [%(levelname)s] : [%(message)s]'
formatter = logging.Formatter(format)
# 将格式对象绑定到输出渠道
sh.setFormatter(formatter)
fh.setFormatter(formatter)

mylog.debug('----------调试信息----------')
mylog.info('----------常规输出----------')
mylog.warning('----------警告信息----------')
mylog.error('----------报错信息----------')
mylog.critical('--------严重错误信息--------')