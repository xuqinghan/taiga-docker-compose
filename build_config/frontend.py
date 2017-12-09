from . import util
import os
from . import download_src
import subprocess


def render(f_name_base, config):
    '''渲染frontend路径下的文件'''
    f_name_base = 'frontend/{0}'.format(f_name_base)
    return util.render(f_name_base, config)


def get_src(config):

    if (not os.path.exists(config['FRONTEND_SRC_HOST'])) or config['RE_CLONE_SRC_FROM_GIT']:
        # source code not exists or need repeat git clone
        download_src.download(
            config['FRONTEND_GIT_REPO'], config['FRONTEND_SRC_HOST_BASE'])
        # subprocess.run('docker stop taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rm taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rmi taigadockercompose_api', shell=True)


def frontend(config):
    '''taiga frontend需要的配置文件'''
    #如果不存在，创建  配置文件根目录
    util.build_dir(config['FRONTEND_CONFIG_HOST'])

    render('conf.json', config)
    render('nginx_front.conf', config)
    render('supervisord.conf', config)
    #docker image
    render('dockerfile', config)
    #render('taiga.ini', config)
    #render('circus.conf', config)

    #下载taiga-back git源码
    get_src(config)


