import os
import time

from win11toast import toast


def get_now_sec():
    return time.localtime(time.time()).tm_hour * 3600 + time.localtime(time.time()).tm_min * 60 + time.localtime(
        time.time()).tm_sec


def format_seconds(seconds):
    t_m, t_s = divmod(seconds, 60)
    t_h, t_m = divmod(t_m, 60)
    return str(int(t_h)).zfill(2) + ":" + str(int(t_m)).zfill(2) + ":" + str(int(t_s)).zfill(2)


def shutdown():
    time.sleep(120)
    show_toast(1)
    time.sleep(30)
    os.system("shutdown -s -t 30")
    os.system("start /MAX .")
    exit()


def show_toast(st):
    toast('AutoShutdown', '计算机将在' + str(st) + '分钟后关闭')