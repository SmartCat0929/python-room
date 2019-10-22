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

ret=re.findall("h[e, ,l]l","h lo world wh\tll") #表示e或者 或者l
print(ret)
ret=re.findall("h[e-l]l","hglo world wh\tll")  #表示e-l的意思
print(ret)
ret=re.findall("h[e,*，.]l","h*lo wh.ld wh\tll") #取消元字符的特殊功能
print(ret)
ret=re.findall("[1-9，a-z,A-Z]","12ad5ADGH")# 字符集 []  [a,b]代表a或者b的意思;
print(ret)
# ^放在[]里面的，表示 取反
ret=re.findall("[5,G]","12ad5ADGH")  #除去5和G的所有展示
print(ret)
ret=re.findall("[^5,G]","12ad5ADGH")  #除去5和G的所有展示
print(ret)

# 元字符 \   反斜杠后边跟元字符去除特殊功能，跟普通字符实现特殊功能

print(re.findall("\d{8}","fauisdlhf12334321456785322"))   #\d   匹配任何十进制数，相当于 0-9
print(re.findall("\slhf","fauisd lhf12334321456785322"))  #\s   匹配任何空白字符，相当于[\t\n\r\f\v]
print(re.findall("\Slhf","fauisdlhf12334321456785322"))  #\w   匹配任何非空白字符，相当于[^ \t\n\r\f\v]
print(re.findall("\W","fauD5 3\r22"))  #\W   匹配任何非字母数字字符，相当于[^ 0-9a-zA-Z]
print(re.findall(r"3\b","fau3D53 3\r22"))  #\b   匹配特殊字符的边界，此例中包括3后面的空格以及\r

###########
# search  扫描整个字符串并返回第一个匹配成功的结果
print(re.search("sb","dfsfhjhsdi88sbjiiusb")) #<re.Match object; span=(12, 14), match='sb'>
print(re.search("sb","dfsfhjhsdi88s1bjiius1b")) #None
print(re.search("sb\?","dfsfhjhsdi88s1bjiiusb?").group()) #sb? 反斜杠后边跟元字符去除特殊功能
print(re.search("sb","dfsfhjhsdi88sbjiiusb").group()) #group 显示结果

ret=re.findall(r"\\","abc\de")
print(ret)
ret=re.findall(r"\babc","abc\de") #r表示原生，用re语言解析
print(ret)

#（）分组  | 或者，优先展现左边的
print(re.search("(as)+","sddhjhjasasashd").group())
print(re.search("4|as+","sd4dhjhjash4d").group())

#正则表达式的方法
# 1. findall(): 所有结果都返回到一个列表里
# 2. search(): 返回匹配后的第一个对象，对象可以调用group
# 3. match(): 只在字符串开始进行匹配
# 4. split():将给定值作为分隔符
# 5. sub(): 进行替换

print(re.split("3","868u3khy"))
print(re.split("[3,j]","3868u3jkhy"))#['', '868u', '', 'khy']

ret=re.sub("a..s","rfft","utuuahusyu")
print(ret)