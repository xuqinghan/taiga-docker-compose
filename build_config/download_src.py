import os
from . import util
#from subprocess import Popen
import subprocess

# git clone 需要空文件夹 fatal: 目标路径 'taiga-back' 已经存在，并且不是一个空目录。



    


def fetch_from_git(git_repo):
    cmd = 'git clone {0}'.format(git_repo)
    #Popen(cmd, shell=True)
    #Popen.wait()
    subprocess.run(cmd, shell=True)

def download(git_repo, path_src):
    '''从git下载源码到制定位置'''
    #创建文件夹 如果有则先删除
    util.delect_build_dir(path_src)
    #切换当前工作路径
    cwd_backup = os.getcwd()
    os.chdir(path_src)
    # 获取源代码
    try:
        fetch_from_git(git_repo)
    except:
        pass
    #切换回原工作路径
    os.chdir(cwd_backup)


# def down_load_backend(git_repo, BACKEND_SRC_PATH):
#     download(git_repo, BACKEND_SRC_PATH)
