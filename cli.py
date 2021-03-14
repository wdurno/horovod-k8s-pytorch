import os 
import sys 
import yaml 
import argparse 

## args 
parser = argparse.ArgumentParser(description='Distributed Pytorch fitting with Horovod on Kubernetes.') 
parser.add_argument('--config-path', dest='config_path', type=str, default=None, help='path to config file') 
parser.add_argument('--no-docker-build', dest='no_docker_build', action='store_true', help='skip docker build step') 
parser.add_argument('--terraform-destroy', dest='terraform_destroy', action='store_true', help='tears-down everything') 
parser.add_argument('--terraform-destroy-compute', dest='terraform_destroy_compute', action='store_true', \
        help='destroys nodes, retains resource group and acr') 
args = parser.parse_args() 

## constants 
args.HOME = os.environ['HOME']  
args.ROOT = os.getcwd() 

## configure build env 
sys.path.append(os.path.join(args.ROOT, 'src', 'python')) 

## import build libs 
from build.terraform import guarantee_phase_1_architecture, guarantee_phase_2_architecture, terraform_destroy, \
        terraform_destroy_compute
from build.secret import refresh_keys 
from build.docker import docker_build 

## parse config path 
if args.config_path is None: 
    ## setting to default 
    config_path = os.path.join(args.HOME, 'horovod-k8s-pytorch-config.yaml') 
    pass

## load config 
with open(config_path, 'r') as f: 
    args.config = yaml.safe_load(f) 
    pass

if args.terraform_destroy_compute:
    terraform_destroy_compute(args.ROOT, args.config) 
    exit(0) ## TODO need arg-checking logic. Will not terraform_destroy after this point. 
    pass 

if args.terraform_destroy: 
    terraform_destroy(args.ROOT, args.config) 
    exit(0) 
    pass

## use build libs 
guarantee_phase_1_architecture(args.ROOT, args.config) 
refresh_keys(args.ROOT, args.config) 
if not args.no_docker_build: 
    docker_build(args.ROOT, args.config) 
    pass
guarantee_phase_2_architecture(args.ROOT, args.config) 
