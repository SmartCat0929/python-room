count=10
def outer():
    global count
    print(count)
    count=5
    print(count)
outer()
#局部要修改全局变量，前面加上global