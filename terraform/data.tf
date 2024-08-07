
data "azurerm_key_vault_secret" "acr_admin_username" {
  name         = "acr-admin-username"
  key_vault_id = azurerm_key_vault.main.id
}

data "azurerm_key_vault_secret" "acr_admin_password" {
  name         = "acr-admin-password"
  key_vault_id = azurerm_key_vault.main.id
}

data "azurerm_key_vault_secret" "db_username" {
  name         = "db-username"
  key_vault_id = azurerm_key_vault.main.id
}

data "azurerm_key_vault_secret" "db_password" {
  name         = "db-password"
  key_vault_id = azurerm_key_vault.main.id
}

data "azurerm_client_config" "current" {}