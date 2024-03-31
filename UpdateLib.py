import os
import time

import requests

# 地址
api_url = "https://api.github.com/repos/huaxia202020/AutoShutdown"
download_url = "https://github.com/huaxia202020/AutoShutdown/archive/master.zip"
lo_push_time = time.localtime()


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
    global lo_push_time
    lo_push_time = time.localtime(new_time)
    print("最后更新时间:{}-{}-{} {}:{}".format(lo_old_time.tm_year, lo_old_time.tm_mon,
                                               lo_old_time.tm_mday, lo_old_time.tm_hour,
                                               lo_old_time.tm_min))
    print("最新推送时间:{}-{}-{} {}:{}".format(lo_push_time.tm_year, lo_push_time.tm_mon,
                                               lo_push_time.tm_mday, lo_push_time.tm_hour,
                                               lo_push_time.tm_min))

    if not old_time:
        old_time = all_info["pushed_at"]
    if new_time > old_time:
        return True
    else:
        return False
