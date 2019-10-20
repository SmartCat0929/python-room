import logging
logging.basicConfig(level=logging.DEBUG,   #以debug为起始值
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')      #以文件形式输出
# Sun, 20 Oct 2019 19:06:57 logging模块.py[line:8] DEBUG debug message
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')  #屏幕输出
# 输出:
# WARNING:root:warning message
# ERROR:root:error message
# CRITICAL:root:critical message
# 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET


