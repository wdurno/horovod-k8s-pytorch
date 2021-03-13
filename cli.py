import os 
import sys 
import yaml 
import argparse 

## args 
parser = argparse.ArgumentParser(description='Distributed Pytorch fitting with Horovod on Kubernetes.') 
parser.add_argument('--config', dest='config', type=str, default=None, help='path to config file') 
parser.add_argument('--no-docker-build', dest='no_docker_build', action='store_true', help='skip docker build step') 
args = parser.parse_args() 

## constants 
args.HOME = os.environ['HOME']  
args.ROOT = os.getcwd() 

## configure build env 
sys.path.append(os.path.join(args.ROOT, 'src', 'python')) 

## import build libs 
from python.build.terraform import guarantee_phase_1_architecture 

## parse config path 
if args.config_path is None: 
    ## setting to default 
    config_path = os.path.join(args.HOME, 'horovod-k8s-pytorch-config.yaml') 
    pass

## load config 
with open(config_path, 'r') as f: 
    args.config = yaml.safe_load(f) 
    pass

# TODO use build libs 

