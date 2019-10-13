# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 生成器的优点：节约内存，类似于厨师上菜
# 生成器一共两种创建方式：1
# s=(x*2 for x in range(4))
# # print(s) #<generator object <genexpr> at 0x02FBCDB0>
# # #生成器就是一个可迭代对象
# # print(next(s)) # 等价于 print(s.__next__())
# # for i in s:
# #     print(i)
# #     print(type(i))

def foo():
    print("ok")
    yield 1
    print("ok2")
    yield 2

g=foo()
print(g) #<generator object foo at 0x04380B30>

next(g)
next(g)

for i in foo():
    print (i)
# ok
# # 1
# # ok2
# # 2

# for 后面跟的都是可迭代对象（有iter方法的）

