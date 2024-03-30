import os
import shutil
import time
import zipfile

import requests

api_url = "https://api.github.com/repos/huaxia202020/AutoShutdown"
download_url = "https://github.com/huaxia202020/AutoShutdown/archive/master.zip"


def copy_dir(src_path, target_path):
    if os.path.isdir(src_path) and os.path.isdir(target_path):
        filelist_src = os.listdir(src_path)
        for copy_file in filelist_src:
            path = os.path.join(os.path.abspath(src_path), copy_file)
            if os.path.isdir(path):
                path1 = os.path.join(os.path.abspath(target_path), copy_file)
                if not os.path.exists(path1):
                    os.mkdir(path1)
                copy_dir(path, path1)
            else:
                with open(path, 'rb') as read_stream:
                    contents = read_stream.read()
                    path1 = os.path.join(target_path, copy_file)
                    with open(path1, 'wb') as write_stream:
                        write_stream.write(contents)
        return True
    else:
        return False


def is_old(old_time):
    # name: x x x / x x x
    all_info = requests.get(api_url).json()
    # 注意8小时的时差
    new_time = time.mktime(time.strptime(all_info["pushed_at"], '%Y-%m-%dT%H:%M:%SZ')) + 3600 * 8
    lo_old_time = time.localtime(old_time)
    lo_new_time = time.localtime(new_time)
    print("最后更新时间:" + "{}-{}-{} {}:{}".format(str(lo_old_time.tm_year), str(lo_old_time.tm_mon),
                                                    str(lo_old_time.tm_mday), str(lo_old_time.tm_hour),
                                                    str(lo_old_time.tm_min)))
    print("最新推送时间:" + "{}-{}-{} {}:{}".format(str(lo_new_time.tm_year), str(lo_new_time.tm_mon),
                                                    str(lo_new_time.tm_mday), str(lo_new_time.tm_hour),
                                                    str(lo_new_time.tm_min)))

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
    # 创建日期文件
    open('last_update.txt', 'a').write(str(time.localtime(time.time())))
    print('更新完成')
else:
    print('无更新')
