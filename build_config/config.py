import pyyaml

with open('./setup-config.yml') as f:
    config = pyyaml.load(f)

#taiga source code
BACKEND_SRC_PATH = '{0}/src'.format(config['back-end']['path'])
BACKEND_GIT_REPO = config['back-end']['git_repo']


#os.popen
