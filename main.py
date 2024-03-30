import datetime
from decimal import Decimal

from MainLib import *

# 数据定义
ShutdownTimes = [['12:00', 35], ['17:15', 55], ['21:30', 5]]
ShutdownTimesSec = []
ShutdownSec = 0
showToastTime = 0
IsShow = False

# 数据整理
for i in ShutdownTimes:
    t = i[0].split(':')
    ShutdownTimesSec.append(int(t[0]) * 3600 + int(t[1]) * 60)
ShutdownTimesSec.sort()
for i in ShutdownTimesSec:
    if i > get_now_sec():
        ShutdownSec = i
        break
for i in ShutdownTimes:
    t = i[0].split(':')
    if int(t[0]) * 3600 + int(t[1]) * 60 == ShutdownSec:
        showToastTime = i[1]

# 排除处理
current_date = datetime.datetime.now().date()
if current_date.weekday() == 6:
    toast('AutoShutdown', '今天为星期日，启用新的关机计划')
    ShutdownTimes = [['17:40', 45], ['21:30', 5]]
if current_date.weekday() == 5:
    pass

# 更新
try:
    import update
except Exception as e:
    print(f'更新时出现错误: {e}')
# 等待
print("下一次关机时间:{}:{}".format(str(time.localtime(ShutdownSec).tm_hour), str(time.localtime(ShutdownSec).tm_min)))
while ShutdownSec > get_now_sec():
    time.sleep(1)
    if not IsShow:
        if ShutdownSec - showToastTime * 60 < get_now_sec():
            show_toast(Decimal((ShutdownSec - get_now_sec()) / 60).quantize(Decimal("0.01"), rounding="ROUND_HALF_UP"))
            IsShow = True

    print('\r关机倒计时:' + format_seconds(ShutdownSec - get_now_sec()), end='')
shutdown()
