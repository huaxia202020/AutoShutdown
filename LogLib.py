import logging
import time

lt=time.localtime(time.time())
logging.basicConfig(filename='{}-{}-{}-ASLog.txt'.format(lt.tm_year,lt.tm_mon,lt.tm_mday),
                    format = '[%(asctime)s - %(name)s - %(funcName)s - %(levelname)s ] %(message)s',
                    level=logging.ERROR)
logger = logging.getLogger('AS')
logger.error("as")