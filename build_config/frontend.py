from . import util
import os
from . import download_src
import subprocess


def render(f_name_base, config):
    '''渲染frontend路径下的文件'''
    f_name_base = 'frontend/{0}'.format(f_name_base)
    return util.render(f_name_base, config)


def render_to_src_dist(f_name_base, config):
    #加载模板
    f_name_template = 'frontend/{0}'.format(f_name_base)
    template = util.load_template(f_name_template)
    #渲染
    content_str = template.render(config)
    #print(content_str)
    #保存
    f_name_src = 'frontend/src/taiga-front-dist/dist/{0}'.format(f_name_base)
    util.save_txt(f_name_src, content_str)

def get_src(config):

    if (not os.path.exists(config['FRONTEND_SRC_HOST'])) or config['RE_CLONE_SRC_FROM_GIT']:
        # source code not exists or need repeat git clone
        download_src.download(
            config['FRONTEND_GIT_REPO'], config['FRONTEND_SRC_HOST_BASE'])
        # subprocess.run('docker stop taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rm taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rmi taigadockercompose_api', shell=True)


def image_container(config):
    SERVICE_NAME = 'frontend'

    util.remove_container(SERVICE_NAME)
    #util.remove_image(SERVICE_NAME)
    CONTEXT = config['front_end']['CONFIG_HOST']
    #util.build_image(CONTEXT, SERVICE_NAME)
    #util.run_container(SERVICE_NAME)

def frontend(config):
    '''taiga frontend需要的配置文件'''
    #如果不存在，创建  配置文件根目录
    util.build_dir(config['FRONTEND_CONFIG_HOST'])
    

    render('nginx_front.conf', config)
    render('supervisord.conf', config)
    #docker image
    render('dockerfile', config)
    #render('taiga.ini', config)
    #render('circus.conf', config)

    #下载taiga-back git源码
    get_src(config)

    #源码路径下 docker-compose.yml中直接挂进去
    render_to_src_dist('conf.json', config)
    image_container(config)
