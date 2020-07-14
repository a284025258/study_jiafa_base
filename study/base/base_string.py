
# format格式化
# str1 = '姓名:{}, 年龄：{}'
# print(str1.format('Jax', 25))

# list1 = [1, 2, 'aA', {'name': 'Jax'}]
# # list1.reverse()
# # list1.sort()
# print(list1)
# import os
# output = os.popen('ipconfig')
# re = output.read()
# output.close()
# print(type(re))
# print(re)

# 字符串转列表 （其他数据类型）
# print(type(eval('[1, 2, 3]')))
#
# print(
# '''***
# 1
# 2
# ***''')
#  __setattr__ 魔术方法
#  __name__ 魔术变量
class Dog(object):
   def  __setattr__(self, k ,v):
       print(k, v)
       super().__setattr__(k, v)

dog = Dog()
setattr(dog, 'name', 'Boy')
print(dog.name)