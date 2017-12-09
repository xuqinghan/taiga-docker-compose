import yaml
import build_config
import os



def load_config(f_name):

    with open(f_name, 'r') as f:
        config = yaml.load(f)

    #backend
    config['BACKEND_GIT_REPO'] = config['back_end']['git-repo']
    config['BACKEND_CONFIG_HOST'] = os.path.abspath(config['back_end']['CONFIG_HOST'])
    config['BACKEND_SRC_HOST'] = os.path.abspath(config['back_end']['SRC_HOST'])
    #容器中位置
    HOME_TAIGA = config['HOME_TAIGA']
    config['BACKEND_SRC_CONTAINER'] = '{0}/{1}'.format(HOME_TAIGA, config['back_end']['SRC_CONTAINER'])
    config['BACKEND_MEDIA_CONTAINER'] = '{0}/media'.format(HOME_TAIGA)
    config['BACKEND_STATIC_CONTAINER'] = '{0}/static'.format(HOME_TAIGA)

    #host中位置
    DATA_HOST = os.path.abspath(config['back_end']['DATA_HOST'])
    config['BACKEND_DATA_HOST'] = DATA_HOST
    config['BACKEND_MEDIA_HOST'] = '{0}/media'.format(DATA_HOST)
    config['BACKEND_STATIC_HOST'] = '{0}/static'.format(DATA_HOST)

    config['BACKEND_PORT'] = config['back_end']['PORT']

    #
    #frontend
    config['FRONTEND_GIT_REPO'] = config['front_end']['git-repo']
    config['FRONTEND_CONFIG_HOST'] = os.path.abspath(
        config['front_end']['CONFIG_HOST'])
    #git clone的工作路径
    config['FRONTEND_SRC_HOST_BASE'] = os.path.abspath(
        config['front_end']['SRC_BASE'])
    #git repo工程名
    config['FRONTEND_BASENAME'] = config['front_end']['BASENAME']
    #git 后的路径
    config['FRONTEND_SRC_HOST'] = '{0}/{1}'.format(config['FRONTEND_SRC_HOST_BASE'], config['FRONTEND_BASENAME'])

    #容器中工程位置
    config['FRONTEND_SRC_CONTAINER'] = '{0}/{1}'.format(
            HOME_TAIGA, config['FRONTEND_BASENAME'])

    # #host中保存数据位置
    # config['FRONTEND_DATA_HOST'] = os.path.abspath('./{0}'.format(config['FRONTEND_BASENAME']))

    #events
    config['EVENTS_GIT_REPO'] = config['events']['git-repo']
    config['EVENTS_CONFIG_HOST'] = os.path.abspath(
        config['events']['CONFIG_HOST'])
    config['EVENTS_SRC_HOST'] = os.path.abspath(config['events']['SRC_HOST'])

    config['EVENTS_SRC_CONTAINER'] = '{0}/{1}'.format(
        HOME_TAIGA, config['events']['SRC_CONTAINER'])

    config['EVENTS_PORT'] = config['events']['PORT']

    #logs backend frontend 和 events 都挂到1个路径下
    config['LOGS_CONTAINER'] = '{0}/logs'.format(HOME_TAIGA)
    config['LOGS_HOST'] = os.path.abspath('./logs')


    return config

config = load_config('./setup-config.yml')

print(config['BACKEND_MEDIA_HOST'])

#config['TAIGA_HOSTNAME'] = '192.168.239.129'


# build all config files for docker backend frontend...
build_config.docker_compose(config)
build_config.backend(config)
build_config.frontend(config)
build_config.events(config)

#subprocess.run('docker-compose up', shell=True)
#print(config['BACKEND_SRC_CONTAINER'])
# docker run -itd -v /home/xuqinghan/taiga-docker-compose/backend/scripts:/scripts --name taigadockercompose_api_1 taigadockercompose_api
