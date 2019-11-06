import logging
from conf import settings


def logger(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)


ch = logging.StreamHandler()
ch.setLevel(settings.LOG_LEVEL)

log_file="%s/log/%s"%(settings.BASE_DIR,settings.LOG_TYPES[log_type])
fh=logging.FileHandler(log_file)
fh.setLevel(settings.LOG_LEVEL)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

return logger()