class Foo:
    def __init__(self):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")
    def __int__(self):
        return 1111
    def __str__(self):
        return "ssss"
obj=Foo()
obj() #对象后面直接加括号,直接调用call

ret=int(obj)
print(ret)

ret=str(obj)
print(ret)  #较常用