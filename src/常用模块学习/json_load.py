import json   #load和loads反序列化方法,将json格式数据解码为python对象

f = open("json_text", "r")

# data = f.read()
# data = json.loads(data)

data = json.load(f)

print(data["聪明猫"])
