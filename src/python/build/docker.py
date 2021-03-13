from util import run

def docker_build(roof, conf): 
    '''
    Builds necessary docker images. 
    Works by 
    1. deploying a build env container, 
    2. copying build dependencies into the container, 
    3. building the image, 
    4. uploading, 
    5. then tearing-down the build env. 
    '''
    pass 

def __deploy_docker_build_env(root, conf): 
    'deploys build env helm chart'
    pass 

def __build(root, conf): 
    'runs a remote docker build'
    pass

def __tear_down_docker_build_env(root, conf): 
    'tears-down build env helm chart'
    pass 

