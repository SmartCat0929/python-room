import os  #os为操作系统
print(os.getcwd()) #获取当前目录
# # os.chdir(r"C:\Users") #改变到哪个目录
# print(os.getcwd()) #获取当前目录
# os.makedirs("abc\\alex\\c")
# os.removedirs("abc\\alex\\c") #只能删除空的文件夹
# dir=os.listdir(r"D:\github\python-room\src\函数")#印出下面的文件
# print (dir)
# os.rename("os模块","os模块学习")
# info=os.stat(".\\ABC")
# print(info.st_size) #文件大小
#
# print(os.sep) #路径分隔符 Windows下为\,linux下为/
# print(os.pathsep)
# print(os.system("dir"))
sss=os.path.split(r"D:\github\python-room\src\函数")
print(sss)
# print(os.path.dirname(sss) )