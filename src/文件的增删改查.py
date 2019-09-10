f = open("小重山","r",encoding ="utf8")
with open("小重山", "r",encoding ="utf8") as f_read, open("小重山2", "w",encoding ="utf8")as f_write:
    number = 0
    for line in f_read:
        number += 1
        if number == 5:
            line = "".join([line.strip(), "hello \n"])
        f_write.write(line)
