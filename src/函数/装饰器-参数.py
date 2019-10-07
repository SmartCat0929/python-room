import time
def logger(flag): #装饰器的参数设置
    def show_time(f):
        def wrapper(*a, **b):
            start_time = time.time()
            f(*a, **b)
            end_time = time.time()
            print('spend %s' % (end_time - start_time))
            if flag=="true":
                print("日志记录")
        return wrapper

    return show_time

@logger("true")  # add=show_time(add)
def add(*a, **b): #不定长参数
    sums=0
    for i in a:
        sums+=i
    print(sums)
    time.sleep(1)
add(2, 4)

@logger("ooo") #foo1 = show_time(foo1)
def foo1():
    print("foo1....")
    time.sleep(4)
foo1() #相当于执行了inner函数