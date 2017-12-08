import yaml
import build_config
import subprocess
import os

def load_config(f_name):

    with open(f_name, 'r') as f:
        config = yaml.load(f)

    #taiga source code
    config['BACKEND_GIT_REPO'] = config['back_end']['git-repo']
    config['BACKEND_SRC_HOST'] = config['back_end']['SRC_HOST']
    config['BACKEND_SRC_CONTAINER'] = config['back_end']['SRC_CONTAINER']
    config['BACKEND_MEDIA_CONTAINER'] = '{0}/media'.format(config['BACKEND_SRC_CONTAINER'])
    config['BACKEND_STATIC_CONTAINER'] = '{0}/static'.format(config['BACKEND_SRC_CONTAINER'])
    config['DATA_HOST'] = config['back_end']['DATA_HOST']
    config['BACKEND_MEDIA_HOST'] = '{0}/media'.format(config['DATA_HOST'])
    config['BACKEND_STATIC_HOST'] = '{0}/static'.format(config['DATA_HOST'])

    return config



# docker-compose.yml

config = load_config('./setup-config.yml')

#config['TAIGA_HOSTNAME'] = '192.168.239.129'

build_config.docker_compose(config)
build_config.backend(config)

#download taiga-back source code

src_path = '{0}/taiga-back'.format(config['BACKEND_SRC_HOST'])

if (not os.path.exists(src_path)) or config['RE_CLONE_SRC_FROM_GIT']:
    # source code not exists or need repeat git clone
    build_config.download(config['BACKEND_GIT_REPO'], config['BACKEND_SRC_HOST'])
    subprocess.run('docker stop taigadockercompose_api_1', shell=True)
    subprocess.run('docker rm taigadockercompose_api_1', shell=True)
    subprocess.run('docker rmi taigadockercompose_api', shell=True)

#subprocess.run('docker-compose up', shell=True)
#print(config['BACKEND_SRC_CONTAINER'])
# docker run -itd -v /home/xuqinghan/taiga-docker-compose/backend/scripts:/scripts --name taigadockercompose_api_1 taigadockercompose_api
