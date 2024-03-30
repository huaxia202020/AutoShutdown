import shutil
import zipfile

from UpdateLib import *

# 更新日志初始化
if not os.path.exists('./UpdateLogs.txt'):
    open('./UpdateLogs.txt', 'w').write(str(time.localtime(time.time())) + "\n")

# 更新流程
old = is_old(os.path.getmtime('./UpdateLogs.txt'))
if old:
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
    open('./UpdateLogs.txt', 'a').write(str(time.localtime(time.time())) + "\n")
    print('已完成从GitHUb的同步更新')
else:
    print('AS在GitHub中无新的推送')
