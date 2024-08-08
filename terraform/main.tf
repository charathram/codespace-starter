provider "azurerm" {
  features {}
}

locals {
  database_url = "postgresql+psycopg2://${data.azurerm_key_vault_secret.db_username.value}:${data.azurerm_key_vault_secret.db_password.value}@${azurerm_postgresql_server.main.fqdn}/${var.postgresql_database_name}?sslmode=require"
}


resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_container_registry" "main" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_linux_web_app" "main" {
  name                = var.app_service_name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  app_settings = {
    WEBSITES_PORT = "8000"
    DATABASE_URL  = local.database_url
  }

  site_config {
    always_on = true
  }

  identity {
    type = "SystemAssigned"
  }

  depends_on = [azurerm_container_registry.main]
}

resource "azurerm_service_plan" "main" {
  name                = var.app_service_plan_name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku_name            = "S1"
  os_type             = "Linux"
}

resource "azurerm_key_vault_secret" "db_username" {
  name         = "db-username"
  value        = var.postgresql_admin_username
  key_vault_id = azurerm_key_vault.main.id
}

resource "azurerm_key_vault_secret" "db_password" {
  name         = "db-password"
  value        = random_password.password.result
  key_vault_id = azurerm_key_vault.main.id
}

resource "azurerm_postgresql_server" "main" {
  name                          = var.postgresql_server_name
  location                      = azurerm_resource_group.main.location
  resource_group_name           = azurerm_resource_group.main.name
  administrator_login           = data.azurerm_key_vault_secret.db_username.value
  administrator_login_password  = data.azurerm_key_vault_secret.db_password.value
  version                       = "11"
  sku_name                      = "B_Gen5_1"
  storage_mb                    = 5120
  backup_retention_days         = 7
  public_network_access_enabled = true
  ssl_enforcement_enabled       = true
}

resource "azurerm_postgresql_database" "main" {
  name                = var.postgresql_database_name
  resource_group_name = azurerm_resource_group.main.name
  server_name         = azurerm_postgresql_server.main.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}
resource "azurerm_key_vault" "main" {
  name                = "${var.prefix}-kv"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku_name            = "standard"

  tenant_id = data.azurerm_client_config.current.tenant_id
}

resource "azurerm_key_vault_access_policy" "main" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  secret_permissions = ["Get", "List", "Set", "Delete", "Recover", "Backup", "Restore", "Purge"]
}

resource "azurerm_key_vault_secret" "acr_admin_username" {
  name         = "acr-admin-username"
  value        = azurerm_container_registry.main.admin_username
  key_vault_id = azurerm_key_vault.main.id
}

resource "azurerm_key_vault_secret" "acr_admin_password" {
  name         = "acr-admin-password"
  value        = azurerm_container_registry.main.admin_password
  key_vault_id = azurerm_key_vault.main.id
}

resource "random_password" "password" {
  length           = 16
  special          = true
  override_special = "_%@"
  keepers = {
    # This value is arbitrary and can be anything. Changing it will
    # trigger the password to be regenerated.
    version = "1"
  }
}