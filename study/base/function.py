def add(a, b):
    return a + b


def subtraction(a=1, b=2):
    return a - b


# print(add(1, 5))
# print(subtraction(2, 5))


def fun1(a, *b):
    print(b)
    sum1 = 0
    sum1 += a
    for i in b:
        sum1 += i
    return sum1


# print(fun1(1, 2, 3, 4))


def fun2(a, *b, **c):
    print(f'{a}\n{b}\n{c}')


# fun2(123, 1, 2, 3, 'int', {'name': 'Jax', 'age': 25}, {'name', 'Bob'}, name='Jax', gender='M')


def fun3():
    a = 1
    print(a)

    def fun4():
        a = 2
        print(a)

    fun4()


# fun3()

# fun5 = lambda x, y: x if x >= y else y
# print(fun5(1, 4))

def fun5(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fun5(n-1) + fun5(n-2)


for i in range(1, 21):
    print(fun5(i))
