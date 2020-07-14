# -*- coding: utf-8 -*-
import random

print(random.random())
print(random.uniform(1, 3))
print(random.randint(1, 3))  # [1,3]
print(random.randrange(1, 3))  # [1,3)
print(random.choice('python'))  # 随机选择一个字符
list1 = list((1, 2, 3, 4))
random.shuffle(list1)  # 随机打乱
print(list1)
print(random.sample(list1, 2))  # 随机截取指定长度的片段 不改变原来的顺序
print(list1)

