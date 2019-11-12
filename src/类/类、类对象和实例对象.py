class C:
    def C1(self):
        count = 1
        print("我是猫猫")


a = C()
b = C()
a.C1()
b.C1 = "我是猪猪"
print(b.C1)
a.C1()
b.C1()   #属性名与方法名相同，属性名会覆盖方法，从而导致报错
#
# a.count+=2
# print(a.count,b.count)
