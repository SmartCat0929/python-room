import time
 # print(help(time))
# print(time.time()) #1571064069.435492 时间戳
# time.sleep(3)
# print(time.clock())#CPU执行时间
# print(time.gmtime()) #结构化时间 time.struct_time(tm_year=2019, tm_mon=10, tm_mday=14, tm_hour=14, tm_min=43, tm_sec=19, tm_wday=0, tm_yday=287, tm_isdst=0)
print(time.localtime()) #time.struct_time(tm_year=2019, tm_mon=10, tm_mday=14, tm_hour=22, tm_min=47, tm_sec=39, tm_wday=0, tm_yday=287, tm_isdst=0)
struct_time=time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) #字符串时间
print(time.strptime("2019-10-14 22:54:15","%Y-%m-%d %H:%M:%S"))
a=time.strptime("2019-10-14 22:54:15","%Y-%m-%d %H:%M:%S")
print(a.tm_yday)
print((time.ctime()))
print((time.ctime(1)))
print((time.ctime(2))) #以诞生时间为基础加上多少秒
print(time.mktime(time.localtime())) #转化为时间戳




import datetime
print(datetime.datetime.now())