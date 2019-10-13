#生成器都是迭代器，迭代器不一定是生成器
# l=[1,2,3,4]
# d=iter(l)
# print(d) #<list_iterator object at 0x0032EE70>

# 迭代器：
# 1. 有iter方法
# 2. 有next方法
# print(next(d))
# print(next(d))
# print(next(d))

# for 循环内部三件事：
# 1. 调用可迭代对象的iter方法返回一个迭代器对象；
# 2. 调用迭代器对象的next方法；
# 3. 处理stopiteration
from collections import Iterable,Iterator
l=[1,2,3,4]
d=iter(l)
print(d)
print(isinstance(l,list))
print(isinstance(l,Iterable))
print(isinstance(l,Iterator))
