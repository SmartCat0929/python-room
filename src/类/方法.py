# 方法
# ----普通方法，保存在类中，由对象来调用

class Foo:

    def bar(self):
        print("bar")

obj=Foo()
obj.bar()

# 或者  Foo.bar()


# -----静态方法-保存在类中，类直接访问
class Foo:
    def bar(self):
        print("bar")
    @staticmethod
    def bar1():
        #静态方法不需要传入对象,self不必须，可以由类直接调用
        print("barbaric")

obj=Foo()
obj.bar()

Foo.bar1()

#----类方法-保存在类中，类直接访问,cls参数是当前类
class Foo:

    def bar(self):
        print("bar")
    @staticmethod
    def bar1():
        print("barbaric")
    @classmethod
    def bar2(cls):
        print("classmd")

obj=Foo()
obj.bar()

Foo.bar1()

#应用场景
# 如果对象中需要保存一些值，执行某功能时，需要使用对象中的值---普通方法
# 不需要任何对象中的值，静态方法