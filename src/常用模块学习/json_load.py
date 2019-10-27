import json

f = open("json_text", "r")

# data = f.read()
# data = json.loads(data)

data = json.load(f)

print(data["聪明猫"])
