# set1 = {'python', 3.14, 233, (1, 2, 3)}
# print(type(set1))
# print(set1)
# # dict1 = {}
# # print(type(dict1))
# # set2 = set()
# # print(type(set2))
# # set2 = set('python')
# # print(set2)
# # set1.add("hello")
# # print(set1)
# set2 = {'hello', 'python', 'world'}
# set1.update(set2)
# print(set1)
# set2.pop()
# # set2.remove('hello')
# # set2.discard('hello')
# set2.clear()
# print(set2)
# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 4, 5}
# print(1 in set1)

def add(*args, **kwargs):
    print(sum(args) + sum(kwargs.values()))

add(1, 2, 3, a=4)