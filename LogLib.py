import logging
import time
import os
lt=time.localtime(time.time())
if not os.path.exists('./logs'):
    os.makedirs('./logs')
logging.basicConfig(filename='./logs/{}-{}-{}-AS-Log.txt'.format(lt.tm_year,lt.tm_mon,lt.tm_mday),
                    format = '[%(asctime)s - %(name)s - %(funcName)s - %(levelname)s ] %(message)s',
                    level=logging.ERROR)
logger = logging.getLogger('AS')