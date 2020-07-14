# def fun1():
#     print("hello world")
#
#
# print(fun1)
# print(type(fun1))
# fun2 = fun1
# fun2()


def fun1(n):
    print('hello')

    def fun2(m):
        print('world')
        print((n + m)**(n + m))
    print('!')
    return fun2


# print(fun1())
fun3 = fun1(1)
print('---------萌萌哒分割线---------')
fun3(2)

# print('---------萌萌哒分割线---------')
# fun4 = fun1
# print('---------萌萌哒分割线---------')
# fun4(5)

