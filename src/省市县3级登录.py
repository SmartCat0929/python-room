province1 = {
    "浙江": {"杭州": ["上城区", "下城区", "拱墅区", "西湖区", "江干区", "滨江区", "余杭区", "萧山区", "富阳区", "临安区"],
           "湖州": ["吴兴区", "南浔区", "长兴县", "安吉县", "德清县"],
           "嘉兴": ["南湖区", "秀洲区", "平湖市", "海宁市", "嘉善县", "海盐县"]
           },
    "江苏": {"南京": ["鼓楼区", "玄武区", "建邺区", "秦淮区", "雨花台区", "栖霞区", "六合区", "浦口区", "江宁区", "溧水区", "高淳区"],
           "苏州": ["姑苏区", "虎丘区", "吴中区", "相城区", "吴江区", "常熟市", "张家港市", "昆山市", "太仓市"],
           "无锡": ["梁溪区", "锡山区", "惠山区", "滨湖区", "新吴区", "江阴", "宜兴"]
           },
}

flag = 0
while True:
    print("当前有以下省份可供选择：",list(province1.keys()))
    province_choose=input("你想登录哪一个省：")
    while True:
        print("该省有以下城市可供选择:",list(province1[province_choose]))
        city_choose=input("你想登录哪一个城市[back:返回上一层]：")
        if city_choose == 'back':
            flag = 1
            break
        else:
            print("该市有以下区县可供选择：",province1[province_choose][city_choose])
            area_choose=input("你想登录哪一个区县[back:返回上一层]：")
            if area_choose == "back":
                continue
            else:
                print("你已经进入了",area_choose,"权限界面。")
                flag = 2
                break
    if flag == 2:
        break


