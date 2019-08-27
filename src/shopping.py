commodity = [["iphones6s", 5000],
             ["macbook", 9000],
             ["coffee", 32],
             ["pythonbook", 80],
             ["bicycle", 1500]
             ]
salary = input("please input your salary:")
shopping_car = []
if salary.isdigit():
    salary = int(salary)
    while True:
        # 打印商品内容
        for i, j in enumerate(commodity, 1):
            print(i, ">>>>", j)
        # 引导用户选择商品
        choise = input("选择购买的商品编号[退出：q]: ")
        if choise.isdigit():
            choise = int(choise)
            if choise >= 1 and choise <= len(commodity):
                p_item = commodity[choise - 1]
                if p_item[1] < salary:
                    salary -= p_item[1]
                    shopping_car.append(p_item)
                else:
                    print("余额不足，还剩%s" % salary)
                print(p_item)
            else:
                print("编码不存在")
        elif choise == "q":
            print("您已经购买以下商品")
            for i in shopping_car:
                print(i)
            print("您还剩%s元钱" % salary)
            break
        else:
            print("invalid input")
