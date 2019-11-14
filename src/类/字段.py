class Province:
    # 这里的country是静态字段，属于类，执行时可以通过对象访问，也可以通过类访问
    country = "中国"

    # name普通字段，属于对象，执行只能通过对象访问
    def __init__(self, name):
        self.name = name

    # appear是方法，调用时直接加括号
    def appear(self):
        print(self.name)


henan = Province("河南")
hebei = Province("河北")

print(Province.country)
henan.appear()
hebei.appear()

