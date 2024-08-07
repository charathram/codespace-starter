output "app_service_default_hostname" {
  description = "The default hostname of the App Service"
  value       = azurerm_app_service.main.default_site_hostname
}

output "container_registry_login_server" {
  description = "The login server of the Azure Container Registry"
  value       = azurerm_container_registry.main.login_server
}

output "container_registry_admin_username" {
  description = "The admin username of the Azure Container Registry"
  value       = azurerm_container_registry.main.admin_username
}

output "container_registry_admin_password" {
  description = "The admin password of the Azure Container Registry"
  value       = azurerm_container_registry.main.admin_password
}
