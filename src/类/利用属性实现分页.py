class Devide:
    def __init__(self, current_page):
        try:
            p = int(current_page)
        except Exception as e:
            p = 1

        self.page = p

    @property
    def start(self):
        val = (self.page - 1) * 10
        return val

    @property
    def end(self):
        val = self.page * 10
        return val


ye = []
for i in range(1000):
    ye.append(i)

while True:
    p = input("请输入即将跳转的页码：")
    obj = Devide(p)
    print(ye[obj.start:obj.end])
