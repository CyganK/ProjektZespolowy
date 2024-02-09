terraform {
    required_providers {
        azurerm = {
            source = "azurerm"
            version = "~>3.8.0"
        }
    }
}

provider "azurerm" {
  features {}
  client_id       = "ddfd42e1-e9a2-44fb-aa12-036b044748d2"
  client_secret   = "mVd8Q~sQhaEhKfSeTIkPZOm1Yh9pOmdQ2phZzb4N"
  tenant_id       = "7babbace-799f-4cbd-991a-54446c9b1c8e"
  subscription_id = "ad2a87ce-3a0a-4514-9f49-3653c3b26130"
}
