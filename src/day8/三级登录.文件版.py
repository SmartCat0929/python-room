# 需求：
#     1、展示省市县（数据存在文件中）
#     2、对菜单实现可以增删改省市县
#
# 思路：
#     1、菜单存在文件里面，读取出来是str格式，通过eval(将字符串string对象转化为有效的表达式参与求值运算返回计算结果)转化成字典
#     2、对比原来的功能多了增加（add）、修改（change）、删除（delete）操作，这里就是多几个if判断
#     3、用户操作完之后呢，就需要修改完再以str格式写回文件内

with open("D:/给猫咪的学习资料/python全栈工程师/day08-python 全栈开发-基础篇/三级省市", "r", encoding="utf8") as f:
    # print(temp)
    menu_dict = eval(f.read().strip())
    # print(menu_dict)
flag = True
current_menu = menu_dict  #刚开始就是一级菜单栏
print(current_menu)
menu_list = []

while flag:
    print(menu_list)
    #打印菜单栏内容，跟current_menu有关
    for menu in current_menu:
        print(menu)
    choice_menu = input("请选择需要查询的地区或增加(add)、修改(change)、删除(delete)操作，b返回上一层，q退出：").strip()
    #查询
    if choice_menu in current_menu:
        #将父级菜单加入列表
        menu_list.append(current_menu)
        #变量存储子级菜单
        current_menu = current_menu[choice_menu]
        if not current_menu:
            print("最后一层了")
    #新增
    elif choice_menu=="add":
        add_menu = input("请输入你要增加的内容：")
        if add_menu in current_menu:
            print ("您输入的内容已存在")
        else:
            current_menu[add_menu]={}
    #修改
    elif choice_menu=="change":
        old_menu = input("请输入你要修改的对象")
        if old_menu in current_menu:
            change_menu=input("请输入你要修改的内容")
            current_menu[old_menu]=current_menu[change_menu]
        else:
            print("您要修改的对象不存在")
    #删除
    elif choice_menu=="delete":
        delete_menu=input("请输入你要删除的对象")
        if delete_menu in current_menu:
            current_menu.pop(delete_menu)
        else:
            print("您要删除的对象不存在")
    #返回上一层
    elif choice_menu=="b":
        if menu_list:
            current_menu=menu_list.pop()
        else:
            print ("已经是最高级了")
    #退出
    elif choice_menu=="q":
        flag=false
        if len(menu_list)==0:
            continue
        else:
            current_menu=menu_list(0)
    else:
        print("输入有误")
with open("D:/给猫咪的学习资料/python全栈工程师/day08-python 全栈开发-基础篇/三级省市", "w", encoding="utf8") as f:
    new_menu = str(current_menu)
    f.write(new_menu)




