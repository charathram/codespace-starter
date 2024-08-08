
variable "prefix" {
  description = "A prefix for all resources to ensure uniqueness"
  type        = string
  default     = "crowdbotics-research"
}

variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "crowdbotics-research-rg"
}

variable "location" {
  description = "The Azure region to deploy to"
  type        = string
  default     = "East US"
}

variable "acr_name" {
  description = "The name of the Azure Container Registry"
  type        = string
  default     = "crowdboticsresearchregistry"
}

variable "app_service_plan_name" {
  description = "The name of the App Service plan"
  type        = string
  default     = "crowdbotics-research-app-service-plan"
}

variable "app_service_name" {
  description = "The name of the App Service"
  type        = string
  default     = "crowdbotics-research-app-service"
}

variable "container_image_name" {
  description = "The name of the container image"
  type        = string
  default     = "crowdbotics-research-app"
}

variable "postgresql_server_name" {
  description = "The name of the PostgreSQL server"
  type        = string
  default     = "crowdbotics-research-postgres-server"
}

variable "postgresql_admin_username" {
  description = "The admin username for PostgreSQL"
  type        = string
  default     = "adminuser"
}

variable "postgresql_database_name" {
  description = "The name of the PostgreSQL database"
  type        = string
  default     = "crowdboticsresearchdb"
}
variable "key_vault_name" {
  description = "The name of the Key Vault"
  type        = string
  default     = "crowdbotics-research-keyvault"
}