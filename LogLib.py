import logging
import os
import time

# logger初始化
lt = time.localtime(time.time())
# 创建文件夹
if not os.path.exists('./logs'):
    os.makedirs('./logs')
# 初始化日志配置
logging.basicConfig(filename='./logs/{}-{}-{}-AS-Log.txt'.format(lt.tm_year, lt.tm_mon, lt.tm_mday),
                    format='[%(asctime)s - %(name)s - %(funcName)s - %(levelname)s ] %(message)s',
                    level=logging.DEBUG, encoding='utf-8')
logger = logging.getLogger('AS')
