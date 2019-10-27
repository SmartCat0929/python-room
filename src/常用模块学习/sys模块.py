# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0)
# sys.version        获取Python解释程序的版本信息
# sys.maxint         最大的Int值
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称


# 进度条
import sys,time
for i in range(10):
    sys.stdout.write('#')
    time.sleep(1)
    sys.stdout.flush()

# sys.stdout与print：
# 在python中调用print时，事实上调用了sys.stdout.write(obj+'\n')
# print 将需要的内容打印到控制台，然后追加一个换行符
# 以下两行代码等价：
# sys.stdout.write('hello' + '\n')
# print('hello')