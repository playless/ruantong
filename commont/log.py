import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 日志切割，最大100M，最多50个
# file_handler = logging.handlers.RotatingFileHandler('test_log_file', mode='a', encoding='utf-8',
#                                                     maxBytes=1024*1024*100, backupCount=50)
# file_handler.setLevel(logging.DEBUG)

# 创建控制台输出handler
console_handler = logging.StreamHandler()

# 定义handler输出格式
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
# file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# logger添加handler
# logger.addHandler(file_handler)
logger.addHandler(console_handler)
# logger.info("这是info")