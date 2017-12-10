from . import util
import os
from . import download_src
import subprocess


def render(f_name_base, config):
    '''渲染backend路径下的文件'''
    f_name_base = 'backend/{0}'.format(f_name_base)
    return util.render(f_name_base, config)

def render_script(f_name_base, config):
    '''渲染backend路径下的文件'''
    f_name_base = 'backend/scripts/{0}'.format(f_name_base)
    return util.render(f_name_base, config)

def copy_settings__init__(config):
    '''settings/__init__.py 缺少celery_local import语句'''
    #模板下的名字
    f_name_src = 'backend/settings/__init__.py'
    f_name_dest = 'backend/src/taiga-back/settings/__init__.py'
    util.copy_file(f_name_src, f_name_dest, config)


def copy_taiga_ini(config):
    '''settings/__init__.py 缺少celery_local import语句'''
    #模板下的名字
    f_name_src = 'backend/settings/__init__.py'
    f_name_dest = 'backend/src/taiga-back/settings/__init__.py'
    util.copy_file(f_name_src, f_name_dest, config)





def render_to_src_settings(f_name_base, config):
    #加载模板
    f_name_template = 'backend/settings/{0}'.format(f_name_base)
    template = util.load_template(f_name_template)
    #渲染
    content_str = template.render(config)
    #print(content_str)
    #保存
    f_name_src = 'backend/src/taiga-back/settings/{0}'.format(f_name_base)
    util.save_txt(f_name_src, content_str)


def get_src(config):
    src_path = '{0}/{1}'.format(
        config['BACKEND_SRC_HOST'], config['back_end']['SRC_CONTAINER'])

    if (not os.path.exists(src_path)) or config['RE_CLONE_SRC_FROM_GIT']:
        # source code not exists or need repeat git clone
        download_src.download(
            config['BACKEND_GIT_REPO'], config['BACKEND_SRC_HOST'])
        subprocess.run('docker stop taigadockercompose_api_1', shell=True)
        subprocess.run('docker rm taigadockercompose_api_1', shell=True)
        subprocess.run('docker rmi taigadockercompose_api', shell=True)


def image_container(config):
    SERVICE_NAME = 'api'

    util.remove_container(SERVICE_NAME)
    #util.remove_image(SERVICE_NAME)
    CONTEXT = config['back_end']['CONFIG_HOST']
    #util.build_image(CONTEXT, SERVICE_NAME)
    #util.run_container(SERVICE_NAME)

def backend(config):
    '''taiga backend需要的配置文件'''
    #如果不存在，创建  配置文件根目录
    util.build_dir(config['BACKEND_CONFIG_HOST'])

    #docker image
    render('dockerfile', config)
    #circus
    render('taiga.ini', config)

    #等待db容器启动
    render('wait-for-postgres.sh', config)
    #首次执行 django配置 初始化数据库 
    render_script('checkdb.py', config)
    render_script('entrypoint.sh', config)

    #下载taiga-back git源码
    get_src(config)

    #taiga-back django明确需要
    render_to_src_settings('celery_local.py', config)
    render_to_src_settings('local.py', config)

    #自己修正源码中bug
    copy_settings__init__(config)

    #清除容器 镜像，重建
    image_container(config)
