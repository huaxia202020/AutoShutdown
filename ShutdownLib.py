import os
import time

from win11toast import toast
from tkinter import messagebox
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
    time.sleep(240)
    os.system("shutdown -s -t 60")
    if messagebox.askokcancel("提示", "电脑将在1分钟后关机，是否取消"):
        os.system("shutdown -a")
    exit()


def show_shutdown_toast(st):
    toast('AutoShutdown', '计算机将在{}分钟后关闭'.format(st))
    #  , icon=r".\Shutdown.ico"
