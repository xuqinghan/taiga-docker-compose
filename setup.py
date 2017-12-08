import yaml
import build_config
import subprocess

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
#build_config.download(config['BACKEND_GIT_REPO'], config['BACKEND_SRC_HOST'])

#subprocess.run('docker-compose up', shell=True)
#print(config['BACKEND_SRC_CONTAINER'])
