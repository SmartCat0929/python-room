import random
# random.random(1,2,3)
# print(random.random())
# print(random.randint(1,8)) #包含8
# print(random.choice("hello"))
# print(random.choice(["hello",1,2,[2,3]]))
# print(random.sample("hello",[1,2,[2,3]]))
# print(random.randrange(1,3))#不包含3

def v_code():
    code=""
    for i in range(5):
        add_num=random.choice([random.randrange(10),chr(random.randrange(65,91))])
        code += str(add_num)
    print(code)

v_code()

