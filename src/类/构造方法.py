class Person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def show(self):
        print("%s---%s" % (self.n, self.a))


maomi = Person("聪明猫", "18")
maomi.show()
zhutou = Person("蠢萌猪", "81")
zhutou.show()
