import json #JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。Python3 中可以使用 json 模块来对 JSON 数据进行编解码

dic = {"聪明猫": "张婷婷", "蠢萌猪": "常征"}
f = open("json_text1", "w")

# data = json.dumps(dic)
# f = open("json_text", "w")
data = json.dump(dic,f)
# f.write(data)
f.close()
