from jinja2 import Template
import os
import shutil

dir_base = os.path.split(os.path.realpath(__file__))[0]

def delect_build_dir(path_dir):
    '''如果文件夹存在则删除'''
    if os.path.exists(path_dir):
        shutil.rmtree(path_dir)
    os.mkdir(path_dir)

def build_dir(path_dir):
    '''如果文件夹不存在则创建'''
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)

def load_template(f_name_base):
    '''加载模板'''
    f_name = '{0}/templates/{1}'.format(dir_base, f_name_base)
    template_str = open(f_name, 'r').read()
    return Template(template_str)

def save_txt(f_name_base, content_str):
    '''保存在当前工作路径'''
    f_name = '{0}/{1}'.format(os.getcwd(), f_name_base)
    print('save ', f_name)
    #文件夹,如果不存在先创建
    build_dir(os.path.dirname(f_name))
    #创建文件
    with open(f_name, 'w') as f:
        f.write(content_str)


def render(f_name_base, config):
    #加载模板
    template = load_template(f_name_base)
    #渲染
    content_str = template.render(config)
    #print(content_str)
    #保存
    save_txt(f_name_base, content_str)

def copy_file(f_name_src, f_name_dest,config):
    '''复制，前后名字不一样'''
    f_name_src = '{0}/templates/{1}'.format(dir_base, f_name_src)
    f_name_dest = '{0}/{1}'.format(os.getcwd(), f_name_dest)
    os.popen('cp {0} {1}'.format(f_name_src, f_name_dest))
