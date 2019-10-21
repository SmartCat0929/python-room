import hashlib

m = hashlib.md5()
print(m)

m.update("hello world".encode("utf8"))
print(m.hexdigest())  # 5eb63bbbe01eeed093cb22bb8f5acdc3

m.update("alex".encode("utf8"))
print(m.hexdigest())  # 82bb8a99b05a2d8b0de2ed691576341a

m2 = hashlib.md5()
m2.update("hello worldalex".encode("utf8"))
print(m2.hexdigest())

s = hashlib.sha3_256()  # 常用
s.update("hello world".encode("utf8"))
print(s.hexdigest)
