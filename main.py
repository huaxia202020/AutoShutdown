import os
import time
from decimal import Decimal
from win11toast import toast
import datetime

def GetNowSec():
    return time.localtime(time.time()).tm_hour * 3600 + time.localtime(time.time()).tm_min * 60 + time.localtime(
        time.time()).tm_sec


def format_seconds(seconds):
    t_m, t_s = divmod(seconds, 60)
    t_h, t_m = divmod(t_m, 60)
    return str(int(t_h)).zfill(2) + ":" + str(int(t_m)).zfill(2) + ":" + str(int(t_s)).zfill(2)
def Shutdown():
    time.sleep(120)
    ShowToast(1)
    time.sleep(30)
    os.system("shutdown -s -t 30")
    os.system("start /MAX .")
    exit()


def ShowToast(st):
    toast('AutoShutdown', '计算机将在' + str(st) + '分钟后关闭')



#数据定义
ShutdownTimes = [['12:00', 35], ['17:15', 55],['21:30', 5]]
ShutdownTimesSec = []
ShutdownSec = 0
showToastTime = 0
IsShow = False

current_date = datetime.datetime.now().date()
if current_date.weekday() == 6:
    toast('AutoShutdown', '今天为星期日，启用新的关机计划')
    ShutdownTimes = [['17:40',45], ['21:30', 5]]
if current_date.weekday() == 5:
    exit()






# 数据整理
for i in ShutdownTimes:
    t = i[0].split(':')
    ShutdownTimesSec.append(int(t[0]) * 3600 + int(t[1]) * 60)
ShutdownTimesSec.sort()
for i in ShutdownTimesSec:
    if (i > GetNowSec()):
        ShutdownSec = i
        break
for i in ShutdownTimes:
    t = i[0].split(':')
    if (int(t[0]) * 3600 + int(t[1]) * 60 == ShutdownSec):
        showToastTime = i[1]

# 等待
while (ShutdownSec > GetNowSec()):
    time.sleep(1)
    if not IsShow:
        if ShutdownSec - showToastTime * 60 < GetNowSec():
            print(ShutdownSec - showToastTime * 60)

            ShowToast(Decimal((ShutdownSec - GetNowSec())/60).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP"))
            IsShow = True

    print('\r倒计时:' + format_seconds(ShutdownSec - GetNowSec()), end='')
Shutdown()






