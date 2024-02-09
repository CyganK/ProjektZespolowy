resource "azurerm_resource_group" "rg" {
  name     = "Projekt-Zespolowy"
  location = "West Europe"
}

# Konto Magazynowe
resource "azurerm_storage_account" "sa" {
  name                     = "ProjektZespolowySA"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# Kontener Blob
resource "azurerm_storage_container" "blob_container" {
  name                  = "PZblobContainer"
  storage_account_name  = azurerm_storage_account.sa.name
  container_access_type = "private"
}

resource "azurerm_container_registry" "acr" {
  name                = "ProjektZespolowyACR"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}


# Tworzenie instancji Azure Container Instance
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "aksCluster"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "aksExample"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_role_assignment" "example" {
  principal_id                     = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id
  role_definition_name             = "AcrPull"
  scope                            = azurerm_container_registry.acr.id
  skip_service_principal_aad_check = true
}

