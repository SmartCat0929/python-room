import pickle
#pickle 的默认格式是二进制格式
# 可以使用 pickle 模块把 Python 对象直接保存到文件里，而不需要先把它们转化为字符串再保存，也不需要用底层的文件访问操作把它们写入到一个二进制文件里。
# pickle 模块会创建一个 Python 语言专用的二进制格式，不需要使用者考虑任何文件细节，它会帮你干净利索地完成读写对象操作，唯一需要的只是一个合法的文件句柄。
# 用pickle比你打开文件、转换数据格式并写入这样的操作要节省不少代码行。

def foo():
    print("ok")
data = pickle.dumps(foo)

f = open("PICKLE_text", "wb") #pickle的写入要用wb(二进制模式打开或者读取)
f.write(data)
f.close()
