import shutil

import requests
import time
import os
import zipfile

api_url = "https://api.github.com/repos/huaxia202020/AutoShutdown"
download_url = "https://github.com/huaxia202020/AutoShutdown/archive/master.zip"


def copy_dir(src_path, target_path):
    if os.path.isdir(src_path) and os.path.isdir(target_path):
        filelist_src = os.listdir(src_path)
        for file in filelist_src:
            path = os.path.join(os.path.abspath(src_path), file)
            if os.path.isdir(path):
                path1 = os.path.join(os.path.abspath(target_path), file)
                if not os.path.exists(path1):
                    os.mkdir(path1)
                copy_dir(path, path1)
            else:
                with open(path, 'rb') as read_stream:
                    contents = read_stream.read()
                    path1 = os.path.join(target_path, file)
                    with open(path1, 'wb') as write_stream:
                        write_stream.write(contents)
        return True
    else:
        return False

def is_old(old_time):
    # name: x x x / x x x
    all_info = requests.get(api_url).json()
    #注意8小时的时差
    new_time = time.mktime(time.strptime(all_info["pushed_at"], '%Y-%m-%dT%H:%M:%SZ'))+3600*8
    if not old_time:
        old_time = all_info["pushed_at"]
    if new_time > old_time:
        return True
    else:
        return False

if not os.path.exists('./last_update.txt'):
    open('last_update.txt', 'w').write(str(time.localtime(time.time())))
old = is_old(os.path.getmtime('./last_update.txt'))

if old:
    print('检查到更新')
    myfile = requests.get(download_url)
    open('AS.zip', 'wb').write(myfile.content)
    #解压
    file = zipfile.ZipFile('AS.zip')
    file.extractall('./')
    file.close()
    #清理
    os.remove('AS.zip')
    shutil.rmtree('./AutoShutdown-master/.idea')
    copy_dir('./AutoShutdown-master','./')
    shutil.rmtree('./AutoShutdown-master')
    #创建日期文件
    open('last_update.txt', 'w').write(str(time.localtime(time.time())))
    print('更新完成')
else:
    print('无更新')