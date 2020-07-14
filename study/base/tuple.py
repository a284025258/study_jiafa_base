# tuple1 = ([1, 2, 3], "python", 3.14)
# print(type(tuple1))
# print(tuple1)
# tuple2 = 1,
# print(type(tuple2))
# print(tuple2)
# for i in tuple1:
#     print(i)
# list1 = [1, 2, 3]
# print(list1 in tuple1)  # 查找某个值是否在该元组里
# print(len(tuple1))  # 长度
# list3 = list(tuple1)
# print(type(list3))
# print(type(tuple1))
# tuple3 = tuple(list3)
# print(type(tuple3))

# tuple1 = (i+j for i in('a', 'b', 'c') for j in('a', 'b', 'c') if i != j)
# list1 = list(tuple1)
# print(list1)
# for i in tuple1:
#     print(i)

# tuple1 = 1, 2, 3, 4
# a, b, c, d = tuple1
# print(a, b, c, d)

# set1 = {9, 2}
# list1 = [9, 2]
# tuple1 = (9, 2)
# print(divmod(9, 2))
# print(divmod(*set1))  # 将元组、列表、集合数据分散

# list1 = [1, 3, 5, 7, 9]
# tuple1 = (2, 4, 6, 8, 0)
# set1 = {'I', 'like', 'python'}
# zip1 = zip(set1, list1)
# for i in zip1:
#     print(i)
# print(dict(zip(tuple1, set1)))
