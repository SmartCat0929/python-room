import json

dic = {"聪明猫": "张婷婷", "蠢萌猪": "常征"}
f = open("json_text1", "w")

# data = json.dumps(dic)
# f = open("json_text", "w")
data = json.dump(dic,f)
# f.write(data)
f.close()
