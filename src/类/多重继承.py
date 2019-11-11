class BaseRequest():
    pass


class RequestHander(BaseRequest):

    def foo1(self):
        print("执行1")

    def foo2(self):
        print("执行2")


class Minx:

    def foo2(self):
        print("执行3")


class Son(Minx, RequestHander):
    pass


obj = Son()
obj.foo2()
