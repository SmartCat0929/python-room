


# 关于ccbox----提供选择0或1
# ccbox(msg='Shall I continue?', title=' ', choices=('Continue', 'Cancel'), image=None)
# import sys
# import easygui as g
# if g.ccbox("亲爱的还玩吗?",choices=("还要玩！","算了吧/(ㄒoㄒ)/~~")):
#     g.msgbox("还是不玩了，快睡觉吧！")
# else:
#     sys.exit(0)

# buttombox()----定义按钮
# buttonbox(msg='', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None)
# 可以使用 buttonbox() 定义自己的一组按钮，buttonbox() 会显示一组你定义好的按钮。
# 当用户点击任意一个按钮的时候，buttonbox() 返回按钮的文本内容。如果用户取消取消或者关闭窗口，那么会返回默认选项（第一个选项）。请看例子：
# import easygui as g
# g.buttonbox(msg="你喜欢下面哪种水果?",title="",choices=("西瓜","苹果","草莓"))

import easygui as g

msg = "请填写一下信息(其中带*号的项为必填项)"
title = "账号中心"
fieldNames = ["*用户名","*真实姓名","固定电话","*手机号码","QQ","*Email"]
fieldValues = []
fieldValues = g.multenterbox(msg,title,fieldNames)
# print(fieldValues)
while True:
    if fieldValues == None :
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ("【%s】为必填项   " %fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
print("您填写的资料如下:%s" %str(fieldValues))