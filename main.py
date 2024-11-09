# 最小化
import ctypes
import datetime
from ShutdownLib import *

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
os.system("title 计划关机")
# 更新
try:
    if not os.path.exists("./Update.lock"):
        import Update
    else:
        print("更新已锁定")
except Exception as e:
    print(f'更新时出现错误: {e}')
    logger.error(f'更新时出现错误: {e}')
# 数据定义
ShutdownTimes = [['9:10', 45], ['12:25', 45], ['17:10', 45], ['21:30', 5]]
IsShow = True
# 排除处理
current_date = datetime.datetime.now().date()
if current_date.weekday() == 6:
    ShutdownTimes = [['12:15', 45], ['17:40', 45], ['21:30', 5]]
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
    "AS计划关机时间:{}:{}(5分钟延迟)".format(int(ShutdownSec / 3600), int(ShutdownSec % 3600 / 60)))
print("AS计划关机时间:{}:{}(5分钟延迟)".format(int(ShutdownSec / 3600), int(ShutdownSec % 3600 / 60)))
while ShutdownSec > get_now_sec():
    time.sleep(1)
    output_str = "\r"
    # if not IsShow:
    #     output_str += '通知倒计时:' + format_seconds(ShutdownSec - showToastTime * 60 - get_now_sec()) + '  '
    #     if ShutdownSec - showToastTime * 60 < get_now_sec():
    #         show_shutdown_toast(
    #             Decimal((ShutdownSec - get_now_sec()) / 60).quantize(Decimal("1"), rounding="ROUND_HALF_UP"))
    #         IsShow = True
    output_str += '关机倒计时:' + format_seconds(ShutdownSec - get_now_sec())
    print(output_str, end='')
shutdown()
