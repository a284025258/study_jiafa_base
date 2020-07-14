import requests
import math
import random
# myList = [[1, 2, 3, 4], "python", 3.14, True]
# emptyLis = []
# print(myList)
# emptyLis += myList
# print(emptyLis)
# for i in range(len(myList)):
#     print(myList[i])
# copyList = myList * 2
# print(copyList)
# for i in myList:
#     print(i)
# print(4 in myList)
# delList = [1]
# print(3.14 in myList)
# del delList[0]
# print(delList)
# print(max(myList[0]))

# myList = [1, 2, 3, 4, 5]
# print(myList[:-1])
# print(myList[::-1])
# list1 = [1, 2, 1]
# list2 = list1[:]
# print(id(list1))
# print(id(list2))
# print(list1 is list2)  # id不同说明地址不一样is判定为false
# print(list1 == list2)  # 值相同，==判定为true
# myList[0:1] = ['p', 'y', 't', 'h', 'o', 'n', 'y']
# print(myList)
# print(list1.count(0))
# list1.append(list2)  # 追加一个值
# print(list1)
# list1.extend(list2)
# print(list1)  # 追加多个值，用列表扩展列表
# list1.insert(0, '0')
# print(list1)
# # print(list1.pop(0))
# list1.reverse()  # 反向
# print(list1)
# list3 = [9, 1, 5, 7]
# list3.sort()  # 升序
# print(list3)
# list3.sort(reverse=True)  # 降序
# print(list3)

# list1 = [i**2 for i in range(1, 11)]  # 列表生成式
# print(list1)
# list2 = [i+j for i in ['a', 'b', 'c'] for j in ['A', 'B', 'C']]
# print(list2)
# list3 = [i**2 for i in range(1, 11) if i % 3 == 0]
# print(list3)

# list1 = (i**2 for i in range(4))
# for i in range(5):
#     print(next(list1))


# def fib():
#     a, b = 0, 1
#     for i in range(10):
#         b, a = a + b, b
#         yield b
#
#
# g = fib()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# list1 = [1, 'Python', 'program', 'PHP']
# list1 .sort(reverse=True, key=str)
# print(list1)
#
# set1 = set('set')
# print(chr(65))

# x = True
# y = False
# z = False
#
# if x or y and z:
#     print('False')
# else:
#     print("True")

# print(math.log(5, 2))
# print(math.modf(3.1415926))

# print(random.randrange(5, 10, 3))
# print(random.uniform(1, 10))
# print(r'\n')
# print('hello, %s' % 'world')
# tuple1 = 1, 2
# print(type(tuple1))
# del tuple1[0]
