import os
from MyQR import myqr
myqr.run(words="http://a.xiazai163.com/apk7/xiaohongshu_v6.8.0_itmop.com.apk",
         version=5,
         level="H",
         picture="D:\\github\\python-room\\resources\\images\\sea.jpg",
         colorized=True,
         contrast=3.0,
         brightness=1.0,
         save_name="D:\\github\\python-room\\output\\xiaohongshu1.png",
        )