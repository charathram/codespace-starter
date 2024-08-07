output "app_service_default_hostname" {
  description = "The default hostname of the App Service"
  value       = azurerm_linux_web_app.main.default_hostname
}

output "container_registry_login_server" {
  description = "The login server of the Azure Container Registry"
  value       = azurerm_container_registry.main.login_server
}