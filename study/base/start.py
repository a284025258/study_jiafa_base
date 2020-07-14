
import sys
# a, b = 1, 2
# a, b = b, a + b
# print(f'a = {a}\nb = {b}')

# n = 1
# a, b = 0, 1
# while n < 10:
#     a, b = b, a + b
#     n += 1
#     print(a, end=' ')

# grade = int(input('请输入成绩：'))
# if 0 <= grade < 60:
#     print('不及格')
# elif 60 <= grade < 90:
#     print('良好')
# elif 90 <= grade <= 100:
#     print('优秀')
# else:
#     print('输入有误')
#
# i = 1
# for i in range(10, 1):
#     print(i)

# list1 = 'hello'
# print(next(iter(list1)))


# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 5:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myNumber = MyNumber()
# myIter = iter(myNumber)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

# 不可变对象 string number tuple 值传递
# 可变对象 list dict 引用传递
# list1 = [1, 2, 3]
# string = '不可变'
#
#
# def fun1(list_pra):
#     list_pra[0] = 0
#
#
# fun1(list1)
# print(list1)
#
#
# def fun2(string1):
#     string1 = '值传递'
#
#
# fun2(string)
# print(string)

# 关键字参数 不考虑参数顺序
# def fun3(age, name):
#     print(f'name:{name}, age:{age}')
#
# fun3(name='Zhang3', age=25)

# # 默认参数
#
# def fun4(name, age=25):
#     print(f'name:{name}, age:{age}')
#
# fun4('Li4')

# # 不定长参数 参数为tuple类型
# # def fun5(*names):
# #     print(type(names))
# #     print(names)
# #
# # fun5('zhang3', 'li4', 'wang5')
# #
# # # 不定长参数 参数为dict类型
# # def fun6(**names):
# #     print(type(names))
# #     print(names)
# #
# # fun6(name='zhang3', age=25)

# 匿名函数 lambda

# a = lambda x, y: x**y
# print(a(2, 3))
#
# def fun6():
#     pass
#
# print(fun6())

# list1 = [1, 2, 3]
# # list1[len(list1):] = [0, 1]  # 追加元素 等价于 extend()
# # list1.append([1, 2])  # 追加列表
# list1.insert(0, 0)
#
# print(list1)

# for i in sys.argv:
#     print(i)
# print(sys.path)  # 模块搜索路径
# import builtins
# import myImport
# import study.myImport
# import myImport as my
# import study.myImport as my2
# for i in sys.modules:
#     print(f'{i}:\t\t\t\t{sys.modules[i]}')
# myImport.test()
# if 1:
#     a = 1
# print(a)

# def outer():
#     a = 1
#     def inner():
#         nonlocal a
#         a = 10
#     inner()
#     print(a)
#
# outer()
# my2.test()
# a = 1
# def test2():
#     pass
# myImport.test()
# study.myImport.test()
# print(dir())

# from study.myImport import *
# test()
with open('d://test.txt') as f:
    print(f.read())
    for i in f:
        print(f.read())