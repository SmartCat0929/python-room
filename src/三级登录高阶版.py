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
current_layer = province1
parent_layer = []
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == "back":
        if parent_layer:
            current_layer = parent_layer.pop()
    else:
        print("无此项")
