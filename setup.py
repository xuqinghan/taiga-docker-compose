import yaml
import build_config
import os



def load_config(f_name):

    with open(f_name, 'r') as f:
        config = yaml.load(f)

    #taiga source code
    config['BACKEND_GIT_REPO'] = config['back_end']['git-repo']
    config['BACKEND_CONFIG_HOST'] = os.path.abspath(config['back_end']['CONFIG_HOST'])
    config['BACKEND_SRC_HOST'] = os.path.abspath(config['back_end']['SRC_HOST'])
    config['BACKEND_SRC_CONTAINER'] = os.path.abspath(config['back_end']['SRC_CONTAINER'])
    config['BACKEND_MEDIA_CONTAINER'] = '{0}/media'.format(config['BACKEND_SRC_CONTAINER'])
    config['BACKEND_STATIC_CONTAINER'] = '{0}/static'.format(config['BACKEND_SRC_CONTAINER'])
    config['DATA_HOST'] = os.path.abspath(config['back_end']['DATA_HOST'])
    config['BACKEND_MEDIA_HOST'] = '{0}/media'.format(config['DATA_HOST'])
    config['BACKEND_STATIC_HOST'] = '{0}/static'.format(config['DATA_HOST'])

    return config

config = load_config('./setup-config.yml')


#config['TAIGA_HOSTNAME'] = '192.168.239.129'


# build all config files for docker backend frontend...
build_config.docker_compose(config)
build_config.backend(config)

#subprocess.run('docker-compose up', shell=True)
#print(config['BACKEND_SRC_CONTAINER'])
# docker run -itd -v /home/xuqinghan/taiga-docker-compose/backend/scripts:/scripts --name taigadockercompose_api_1 taigadockercompose_api
