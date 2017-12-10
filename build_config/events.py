from . import util
import os
from . import download_src



def render(f_name_base, config):
    '''渲染events路径下的文件'''
    f_name_base = 'events/{0}'.format(f_name_base)
    return util.render(f_name_base, config)

def render_to_src(f_name_base, config):
    #加载模板
    f_name_template = 'events/{0}'.format(f_name_base)
    template = util.load_template(f_name_template)
    #渲染
    content_str = template.render(config)
    #print(content_str)
    #保存
    f_name_src = 'events/src/taiga-events/{0}'.format(f_name_base)
    util.save_txt(f_name_src, content_str)

def get_src(config):

    if (not os.path.exists(config['EVENTS_SRC_HOST'])) or config['RE_CLONE_SRC_FROM_GIT']:
        # source code not exists or need repeat git clone
        download_src.download(
            config['EVENTS_GIT_REPO'], config['EVENTS_SRC_HOST_BASE'])
        # subprocess.run('docker stop taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rm taigadockercompose_api_1', shell=True)
        # subprocess.run('docker rmi taigadockercompose_api', shell=True)


def image_container(config):
    SERVICE_NAME = 'events'

    util.remove_container(SERVICE_NAME)
    util.remove_image(SERVICE_NAME)
    CONTEXT = config['events']['CONFIG_HOST']
    #util.build_image(CONTEXT, SERVICE_NAME)
    #util.run_container(SERVICE_NAME)



def events(config):
    '''taiga events需要的配置文件'''
    #如果不存在，创建  配置文件根目录
    util.build_dir(config['EVENTS_CONFIG_HOST'])
    #for circus
    render('circus.conf', config)
    render('circus.service', config)
    
    render('taiga-events.ini', config)

    #docker image
    render('dockerfile', config)
    #render('taiga.ini', config)
    #render('circus.conf', config)

    #下载taiga-back git源码
    get_src(config)
    #config是源码的一部分
    render_to_src('config.json', config)
    image_container(config)
