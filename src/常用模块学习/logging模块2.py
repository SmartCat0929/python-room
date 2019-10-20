import logging  #采用该方法，既可以用文件输出，也可以用屏幕输出

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test1.log')

# 再创建一个handler，用于输出到控制台（屏幕）
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)
logger.setLevel(logging.INFO)


logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

#2019-10-20 19:36:06,722 - root - DEBUG - logger debug message
# 2019-10-20 19:36:06,723 - root - INFO - logger info message
# 2019-10-20 19:36:06,726 - root - WARNING - logger warning message
# 2019-10-20 19:36:06,726 - root - ERROR - logger error message
# 2019-10-20 19:36:06,726 - root - CRITICAL - logger critical message