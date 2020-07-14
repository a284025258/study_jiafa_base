# -*- coding: utf-8 -*-
import time
import os
from collections.abc import Iterable, Iterator

# print(type(time.localtime()))
# print(time.localtime())
# print(time.mktime(time.localtime()))  # 转struct_time对象为时间戳
# print(time.asctime(time.localtime()))  # 转换时间元组或struct_time对象的格式
# print(time.asctime((2020, 3, 25, 13, 4, 12, 2, 85, 0)))
# print(time.ctime(time.mktime(time.localtime())))  # struct_time对象转换为时间戳的格式
# print(time.strftime("%Y-%m-%d %X", time.localtime()))  # struct_time对象转换为指定格式
# print(time.strptime('2020-10-10 14:25:55', '%Y-%m-%d %X'))  # 转换指定格式为struct_time对象

# print(os.getcwd())
# print(os.path)

# print(isinstance([], Iterable))
list1 = [1, 2, 3]
list1 = iter(list1)
print(type(list1))
print(next(list1))
