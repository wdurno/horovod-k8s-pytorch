from util import run 

def refresh_keys(root, conf): 
    pass 

def __get_kubeconfig(conf):
    tf_prefix = config['terraform_prefix'] 
    resource_group = f'{tf_prefix}_rg'
    cluster_name = f'{tf_prefix}_k8s'
    cmd = f'az aks get-credentials --name {cluster_name} --resource-group {rl_hypothesis_2_resource_group_name} --overwrite-existing'
    run(cmd) 
    pass 

def __get_acr_token(root, config): 
    ## get token in JSON from az cli stdout 
    tf_prefix = config['terraform_prefix'] 
    acr_name = f'{tf_prefix}_acr' 
    cmd = f'az acr show -n {acr_name} -o json' 
    json_str = run(cmd, return_stdout) 
    ## parse JSON and save token 
    token = json_str['passwords'][0]['value']  
    token_path = os.path.join(root, 'secret', 'acr', 'token') 
    with open(token_path, 'w') as f:
        f.write(token) 
        pass
    pass

def __get_acr_server(root, config): 
    ## get server in JSON from az cli stdout 
    tf_prefix = config['terraform_prefix'] 
    acr_name = f'{acr_name}_acr' 
    cmd = f'az acr credential show -n {acr_name} -o json'
    json_str = run(cmd, return_stdout) 
    ## parse JSON and save server 
    server = json_str['loginServer'] 
    server_path = os.path.join(root, 'secret', 'acr', 'server') 
    with open(server_path, 'w') as f: 
        f.write(server) 
        pass
    pass 

