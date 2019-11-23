# class Foo:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#         print("%s%s岁了" % (self.name, self.__age))
#
#     def show(self):
#         return self.__age
#
#
# obj = Foo("smallcat", 18)
# print(obj.name)
# # print(obj.__age)  # 私有
# print(obj.show())


class Foo1:
    __count= "123"
    def __init__(self):
        pass
    def show(self):
        return Foo1.__count
print(Foo1().show())