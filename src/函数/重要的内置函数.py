# 1.fliter(过滤)
# filter(function, sequence)

str = ['a', 'b', 'c', 'd']
def fun1(s):
    if s != 'a':
        return s
ret = filter(fun1, str)

print(list(ret))  # ret是一个迭代器对象,不占用内存，现在采用list进行转化

# 2.map(加标记）
str = [1, 2, 'a', 'b']
def fun2(s):
    return (s + "alvin")
ret = map(fun2, str)

print(ret)  # map object的迭代器
print(list(ret))  # ['aalvin', 'balvin', 'calvin', 'dalvin']


# 3. reduce  据说很重要
from functools import reduce #python要首先引入该行代码
def add1(x, y):
    return x + y
print(reduce(add1, range(1, 101)))  ## 4950 （注：1+2+...+99）
print(reduce(add1, range(1, 101), 20))  ## 4970 （注：1+2+...+99+20）
# 对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用.

# 4.lambda (匿名函数)
# 普通函数与匿名函数的对比：
# 普通函数
def add(a, b):
    return a + b
print (add(2, 3))

# 匿名函数
add = lambda a, b: a + b
print (add(2, 3))