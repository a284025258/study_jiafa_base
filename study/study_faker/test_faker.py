from faker import Faker

faker = Faker(locale='zh_CN')
# name = faker.name()
# address = faker.address()
# profile = faker.simple_profile()
# print(name, address, profile)
# ljust() 左对齐，位数不足6位，尾部补 *
# print(faker.user_name().ljust(6, '*')[0:5])
# d = {'name': 'Jax'}
# for k, v in d.items():
#     print(k, v)
# print(d.items())
# from collections.abc import Iterable
# print(isinstance(d.items(), Iterable))
print(faker.sentence()[:4] + '--项目')