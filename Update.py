import shutil
import time
import zipfile

from UpdateLib import *

# 更新日志初始化
if not os.path.exists('./UpdateLogs.txt'):
    lt=time.localtime(time.time())
    open('./UpdateLogs.txt', 'w').write("日志创建时间:{}-{}-{} {}:{}".format(lt.tm_year,lt.tm_mon,lt.tm_mday,lt.tm_hour,lt.tm_min) + "\n")

# 更新流程
if is_old(os.path.getmtime('./UpdateLogs.txt')):
    print('检查到新的推送,正在下载')
    # 下载
    new_file = requests.get(download_url)
    open('AS.zip', 'wb').write(new_file.content)
    # 解压
    file = zipfile.ZipFile('AS.zip')
    file.extractall('./')
    file.close()
    # 清理
    os.remove('AS.zip')
    shutil.rmtree('./AutoShutdown-master/.idea')
    copy_dir('./AutoShutdown-master', './')
    shutil.rmtree('./AutoShutdown-master')
    # 添加更新日志
    lt = time.localtime(time.time())

    with open('./UpdateLogs.txt', 'a') as ulf:
        ulf.write("同步更新时间:{}-{}-{} {}:{}".format(lt.tm_year,lt.tm_mon,lt.tm_mday,lt.tm_hour,lt.tm_min))
        ulf.write("  拉取版本推送时间：{}-{}-{} {}:{}".format(lo_push_time.tm_year,lo_push_time.tm_mon,lo_push_time.tm_mday,lo_push_time.tm_hour,lo_push_time.tm_min))
        ulf.write("\n")
    print('已完成从GitHUb的同步更新')
else:
    print('AS在GitHub中无新的推送')
