from util import run 

def guarantee_phase_1_architecture(root, config): 
    '''
    builds or verifies existence of sufficient architecture to run phase 1
    inputs:  
      - root: repo root path 
      - config: repo configuration object 
    outputs: None
    side-effects: guarantees phase 1 architecture 
    '''
    __copy_phase_1_tf_files(root) 
    __terraform_apply(root, config) 
    pass

def __copy_phase_1_tf_files(root): 
    'copies phase 1 terraform files from terraform/base/ to terraform_state/' 
    cmd = f'cp {root}/terraform/base/*.tf {root}/terraform_state'
    run(cmd, os_system=True) 
    pass

def __terraform_apply(root, config): 
    'execute `terraform apply` to terraform_state directory'
    ## work from terraform_state directory 
    cmd_part_1 = f'cd {root}/terraform_state' 
    ## apply with variables 
    tf_vars = __get_base_var_str(config) 
    cmd_part_2 = 'terraform apply -auto-approve' + tf_vars 
    ## build command 
    cmd = cmd_part_1 + ' && ' + cmd_part_2 
    ## execute 
    run(cmd, os_system=True) 
    pass 

def __get_base_var_str(config):
    '''
    get terraform cli arg string setting base architecture variables
    '''
    ## unpack config
    subscription_id = config.['subscription_id']
    tenant_id = config['tenant_id']
    tf_prefix = config['terraform_prefix']
    ## build str
    base_var_str = f' -var="subscription_id={subscription_id}"'+\
            f' -var="tenant_id={tenant_id}"'+\
            f' -var="resource_group_name={tf_prefix}_rg"'+\
            f' -var="acr_name={tf_prefix}_acr"'+\
            f' -var="k8s_name={tf_prefix}_k8s"'
    return base_var_str

