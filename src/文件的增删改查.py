# import time
#
# f  = open("小重山2", "w",encoding="utf8")
# data=f.write("hello \n")
# data=f.write("hello2 \n")
# time.sleep(30)
# # print(data)
# f.close()

f = open("小重山","r",encoding ="utf8")
# f1.readline()
# print(f1.readlines())
# print(f1.readline())
# for i in f1.readlines():
#     print(i.strip())
with open("小重山", "r",encoding ="utf8") as f_read, open("小重山2", "w",encoding ="utf8")as f_write:
    number = 0
    for line in f_read:
        number += 1
        if number == 5:
            line = "".join([line.strip(), "hello \n"])
        f_write.write(line)
