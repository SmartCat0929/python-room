user = "apple"
passwd = 123456
user1 = "apple"
passwd1 = 12345678

login_status = "false"

def assessment():
    def login():
        if login_status == false:
            if auth_type == "jingdong":
                username = input("username:")
                password = input("passwd:")
                if user == username and passwd == password:
                    print("welcome ....")
                    home()
                    login_status = true
            elif auth_type == "weixin":
                username1 = input("username:")
                password1 = input("passwd:")
                if user1 == username1 and passwd1 == password1:
                    print("welcome ....")
                    finance()
                    login_status = "true"
        else:
            pass


@assessment(auth_type="jingdong")
def home():
    print("welcome to home page")


@assessment(auth_type="weixin")
def finance():
    print("welcome to finance page")
