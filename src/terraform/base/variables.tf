## phase-1 variables 

variable "subscription_id" {
  type = string
}

variable "tenant_id" {
  type = string
}

variable "resource_group_name" { 
  type = string
  default = "rg"
} 

variable "acr_name" { 
  type = string 
  default = "acr" 
} 

variable "k8s_name" { 
  type = string
  default "k8s"
} 

## phase-2 variables 

variable "number_of_ephemeral_nodes" { 
  type = number
  default = 5
}

variable "ephemeral_node_type" { 
  type = string
  default = "Standard_F2S_v2"
} 

variable "number_of_storage_nodes" { 
  type = number 
  default = 3 
} 

variable "storage_node_type" {
  type = string
  default = "Standard_A2M_v2" 
} 

