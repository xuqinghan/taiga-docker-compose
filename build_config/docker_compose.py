from . import util

def docker_compose(config):
    '''build docker-compose.yml'''
    f_name_base = 'docker-compose.yml'
    return util.render(f_name_base, config)

