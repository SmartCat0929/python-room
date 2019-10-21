import re
# 元字符 . [通配符】代指任意一个字符，除了换行符
ret=re.findall("w..l","hello world wo\tld")
print(ret)

# 元字符 ^ [尖角符】只对开头进行匹配,除了换行符
ret=re.findall("^h..l","hello world wo\tld")
print(ret)

# 元字符 $  只对结尾进行匹配,除了换行符
ret=re.findall("h..l$","hello world wh\tll")
print(ret)

# 元字符 *  [重复匹配] 0到正无穷,取最大数
ret=re.findall("h*l","hehhhhllo world wh\tll")
print(ret)

# 元字符 +  [重复匹配] 1到正无穷
ret=re.findall("h+l","hehhhhllo world wh\tll")
print(ret)

# 元字符 ？  [0,1] 重复0或1
ret=re.findall("h?l","hehhhhllo world wh\tll")
print(ret)

# 元字符 {}  重复任意次数
ret=re.findall("h{3}l","hehhhhllo world wh\tll")
print(ret)
ret=re.findall("h{1,4}l","hehhhhllo world wh\tll")
print(ret)