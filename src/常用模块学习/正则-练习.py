import re
# ret=re.findall("[0-2][0-5][0-5].[0-2][0-5][0-5].[0-2][0-5][0-5]","hugdiifug 25.135.254yugug")
# print(ret)

print(re.search(r"(([01]{0,1}\d{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])","fyudty41.168.1.1"))

print(re.search(r"[01]{0,1}\d{0,1}\d{0,1}\d","fyudty32.168.1.1")) #<re.Match object; span=(6, 8), match='32'>

print(re.search(r"2[0-4]\d","fyudty232.268.1.1")) #<re.Match object; span=(6, 9), match='232'>

print(re.search(r"[05]{0,1}\d","fyudty42.268.2.2")) #<re.Match object; span=(6, 7), match='4'>
print(re.search(r"[05]\d","fyudty42.268.2.2")) #None


print(re.search(r"[05]\d","54fy1udty142.268.2.2")) #<re.Match object; span=(0, 2), match='54'>

print(re.search(r"[05]\d","44fy1udty142.268.2.2")) #None

print(re.search(r"(([01]?\d?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])","fyudty100.168.1.1"))

print(re.findall(r"[01]?\d?\d?\d","442fy001udty142"))