from . import util
import os
from . import download_src
import subprocess


def render(f_name_base, config):
    '''渲染events路径下的文件'''
    f_name_base = 'events/{0}'.format(f_name_base)
    return util.render(f_name_base, config)


def get_src(config):
    src_path = '{0}/{1}'.format(config['EVENTS_SRC_HOST'],
                                config['events']['SRC_CONTAINER'])

    if (not os.path.exists(src_path)) or config['RE_CLONE_SRC_FROM_GIT']:
        # source code not exists or need repeat git clone
        download_src.download(
            config['EVENTS_GIT_REPO'], config['EVENTS_SRC_HOST'])
        # subprocess.run('docker stop taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rm taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rmi taigadockercompose_api', shell=True)


def events(config):
    '''taiga events需要的配置文件'''
    #如果不存在，创建  配置文件根目录
    util.build_dir(config['EVENTS_CONFIG_HOST'])

    render('config.json', config)
    render('taiga-events.ini', config)

    #docker image
    render('dockerfile', config)
    #render('taiga.ini', config)
    #render('circus.conf', config)

    #下载taiga-back git源码
    get_src(config)
