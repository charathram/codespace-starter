variable "prefix" {
  description = "A prefix for all resources to ensure uniqueness"
  type        = string
  default     = "crowdbotics_research"
}

variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "${var.prefix}_rg"
}

variable "location" {
  description = "The Azure region to deploy to"
  type        = string
  default     = "East US"
}

variable "acr_name" {
  description = "The name of the Azure Container Registry"
  type        = string
  default     = "${var.prefix}_registry"
}

variable "app_service_plan_name" {
  description = "The name of the App Service plan"
  type        = string
  default     = "${var.prefix}-app-service-plan"
}

variable "app_service_name" {
  description = "The name of the App Service"
  type        = string
  default     = "${var.prefix}-app-service"
}

variable "database_url" {
  description = "The URL of the database"
  type        = string
  default     = "postgresql+psycopg2://app_user:app_password@db/crowdboticsresearchdb"
}

variable "container_image_name" {
  description = "The name of the container image"
  type        = string
  default     = "${var.prefix}-app"
}

variable "postgresql_server_name" {
  description = "The name of the PostgreSQL server"
  type        = string
  default     = "${var.prefix}-postgres-server"
}

variable "postgresql_admin_username" {
  description = "The admin username for PostgreSQL"
  type        = string
  default     = "adminuser"
}

variable "postgresql_admin_password" {
  description = "The admin password for PostgreSQL"
  type        = string
  default     = "adminpassword"
}

variable "postgresql_database_name" {
  description = "The name of the PostgreSQL database"
  type        = string
  default     = "crowdboticsresearchdb"
}
variable "key_vault_name" {
  description = "The name of the Key Vault"
  type        = string
  default     = "${var.prefix}-keyvault"
}
data "azurerm_key_vault_secret" "db_username" {
  name         = "db-username"
  key_vault_id = azurerm_key_vault.main.id
}

data "azurerm_key_vault_secret" "db_password" {
  name         = "db-password"
  key_vault_id = azurerm_key_vault.main.id
}


