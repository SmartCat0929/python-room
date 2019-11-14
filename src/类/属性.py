class Foo:

    @property
    def goo1(self):
        return 1

    @goo1.setter
    def goo1(self,val):
        print(val)

    @goo1.deleter
    def goo1(self):
        print(666)

obj=Foo()
r=obj.goo1
print(r)   #当做字段来调用，与property呼应

obj.goo1=123  #赋值，与方法.setter呼应

del obj.goo1  #del+名称，与方法.deleter呼应