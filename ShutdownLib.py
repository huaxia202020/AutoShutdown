import os
import time

from win11toast import toast

from LogLib import logger


# 关机函数定义
def get_now_sec():
    return time.localtime(time.time()).tm_hour * 3600 + time.localtime(time.time()).tm_min * 60 + time.localtime(
        time.time()).tm_sec


def format_seconds(seconds):
    t_m, t_s = divmod(seconds, 60)
    t_h, t_m = divmod(t_m, 60)
    return str(int(t_h)).zfill(2) + ":" + str(int(t_m)).zfill(2) + ":" + str(int(t_s)).zfill(2)


def shutdown():
    logger.info("已进入关机进程")
    print("已进入关机进程")
    time.sleep(120)
    show_shutdown_toast(1)
    time.sleep(30)
    os.system("shutdown -s -t 30")
    os.system("start /MAX .")
    exit()


def show_shutdown_toast(st):
    toast('AutoShutdown', '计算机将在{}分钟后关闭,您可以现在关闭程序以取消关机或在30秒后点击程序根目录下的脚本以取消'.format(st))
