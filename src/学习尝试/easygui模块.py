# import easygui
# from easygui import *
# msgbox("hello，cat~")
import easygui as g
import sys

g.msgbox("hi,welcome")
msg = "请问你希望可以学到什么专业知识呢？"
title = "猫猫的梦想"
choices = ["python", "English", "项目管理知识"]
choice = g.choicebox(msg, title, choices)
g.msgbox("你的选择是：" + str(choice), "结果")
msg = "你希望重新选择你的梦想吗？"
title = "请选择"
if g.ccbox(msg, title):
    pass
else:
    sys.exit(0)
