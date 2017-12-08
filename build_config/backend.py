from . import util



def render(f_name_base, config):
    '''渲染backend路径下的文件'''
    f_name_base = 'backend/{0}'.format(f_name_base)
    return util.render(f_name_base, config)

def render_script(f_name_base, config):
    '''渲染backend路径下的文件'''
    f_name_base = 'backend/scripts/{0}'.format(f_name_base)
    return util.render(f_name_base, config)


def backend(config):
    '''taiga backend需要的配置文件'''
    render('celery_local.py', config)
    render('local.py', config)
    render('dockerfile', config)

    render_script('checkdb.py', config)
    render_script('entrypoint.sh', config)

