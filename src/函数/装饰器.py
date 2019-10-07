#装饰器，可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
# 装饰器3要素：
# 1. 作用域 LEGB
# 2. 函数即对象
# 3. 闭包

import time
def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print("spend: %s s" % (end - start))

    return inner

@show_time #foo = show_time(foo) 替换后看起来很屌的样子
def foo():
    print("foo....")
    time.sleep(2)
foo() #相当于执行了inner函数

@show_time #foo1 = show_time(foo1)
def foo1():
    print("foo1....")
    time.sleep(4)
foo1() #相当于执行了inner函数



# def show_time(f):
#     start=time.time()
#     f()
#     end=time.time()
#     print("spend: %s s"%(end-start))
# show_time(foo)
# show_time(foo1)


