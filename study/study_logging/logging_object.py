import logging


class LoggingObject(object):
    def __new__(cls, *args, **kwargs):
        """
        类直接调用，创建对象
        :param args:
        :param kwargs:
        :return:
        """
        # 创建日志收集器
        my_log = logging.getLogger('my_log')
        # 设置日志收集器日志收集等级
        my_log.setLevel(logging.DEBUG)
        # 创建输出渠道
        sh = logging.StreamHandler()
        sh.setLevel(logging.WARNING)
        fh = logging.FileHandler(filename='my_log.log', mode='a', encoding='utf8')
        fh.setLevel(logging.WARNING)
        # 将输出渠道添加到日志收集器
        my_log.addHandler(sh)
        my_log.addHandler(fh)
        # 设置日志格式
        format = '[%(asctime)s] - [%(filename)s --> line:%(lineno)d] - [%(levelname)s] : [%(message)s]'
        formatter = logging.Formatter(format)
        # 将格式对象绑定到输出渠道
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        return my_log

log = LoggingObject()
# if __name__ == '__main__':
#     log = LoggingObject()
#     log.debug('----------调试信息----------')
#     log.info('----------常规输出----------')
#     log.warning('----------警告信息----------')
#     log.error('----------报错信息----------')
#     log.critical('--------严重错误信息--------')