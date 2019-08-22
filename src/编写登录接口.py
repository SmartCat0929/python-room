name = "聪明猫"
password = "1234567"
n = 3
while(n > 0):
    your_name = input("please input your name:")
    your_password = input("please input your password:")
    if your_name == name and your_password == password:
        print("欢迎进入")
        break
    else:
        n = n - 1
        print("你还剩",n,"次机会")
