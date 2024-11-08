import os
import time
import datetime
from time import sleep


from tkinter import messagebox
from LogLib import logger

try:
    import pyautogui
    import win32gui, win32con
    from win11toast import toast
    import requests
except ImportError:
    os.system("pip install win11toast -i https://pypi.tuna.tsinghua.edu.cn/simple some-package")
    os.system("pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple some-package")
    os.system("pip install pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple some-package")
    os.system("pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple some-package")
    import pyautogui
    import win32gui, win32con
    from win11toast import toast
    import requests


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
    if os.path.isfile("Running.lock"):
        os.remove("Running.lock")
    time.sleep(240)
    sleep(1)
    window = win32gui.GetForegroundWindow()

    pyautogui.hotkey("win", "d")
    os.system("shutdown -s -t 60")
    if messagebox.askokcancel("提示",
                              "电脑将在1分钟后关机\n点击确定延迟5分钟其间不会再有任何提示\n点击取消将取消关机计划"):
        os.system("shutdown -a")
        os.system("shutdown -s -t 300")
    else:
        os.system("shutdown -a")
    win32gui.SetForegroundWindow(window)
    win32gui.ShowWindow(window, win32con.SW_NORMAL)
    print(win32gui.GetWindowText(window))
    sleep(1)
    exit()


def show_shutdown_toast(st):
    toast('AutoShutdown', '计算机将在{}分钟后关闭'.format(st))
    #  , icon=r".\Shutdown.ico"
