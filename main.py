import datetime
from decimal import Decimal

from ShutdownLib import *

os.system("title 自动关机脚本")

# 更新
try:
    import Update
except Exception as e:
    print(f'更新时出现错误: {e}')

# 数据定义
ShutdownTimes = [['12:00', 35], ['17:15', 55], ['21:30', 5]]
IsShow = False

# 排除处理
current_date = datetime.datetime.now().date()
if current_date.weekday() == 6:
    toast('AutoShutdown', '星期日，启用新的关机计划')
    ShutdownTimes = [['17:05', 45], ['21:30', 5]]
if current_date.weekday() == 5:
    pass

# 数据整理
# 排序
ShutdownTimesSec = []
for i in ShutdownTimes:
    t = i[0].split(':')
    ShutdownTimesSec.append(int(t[0]) * 3600 + int(t[1]) * 60)
ShutdownTimesSec.sort()
# 找出最近的关机时间
ShutdownSec = 0
for i in ShutdownTimesSec:
    if i > get_now_sec():
        ShutdownSec = i
        break
# 找出提示时间
showToastTime = 0
for i in ShutdownTimes:
    t = i[0].split(':')
    if int(t[0]) * 3600 + int(t[1]) * 60 == ShutdownSec:
        showToastTime = i[1]



# 等待
logger.info(
    "AS关机倒计时已启动,关机时间:{}:{}(3分钟延迟)".format(int(ShutdownSec / 3600), int(ShutdownSec % 3600 / 60)))
print("AS关机倒计时已启动,关机时间:{}:{}(3分钟延迟)".format(int(ShutdownSec / 3600), int(ShutdownSec % 3600 / 60)))
while ShutdownSec > get_now_sec():
    time.sleep(1)
    if not IsShow:
        if ShutdownSec - showToastTime * 60 < get_now_sec():
            show_shutdown_toast(Decimal((ShutdownSec - get_now_sec()) / 60).quantize(Decimal("0.1"), rounding="ROUND_HALF_UP"))
            IsShow = True

    print('\r关机倒计时:' + format_seconds(ShutdownSec - get_now_sec()), end='')
shutdown()
