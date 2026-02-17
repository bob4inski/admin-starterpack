terraform {
  required_version = ">= 0.13"

  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = ">= 0.69.0"
    }
  }

  backend "s3" {
    bucket = "private-terraform"
    endpoints = {
      s3 = "https://storage.yandexcloud.net"
    }
    key    = "terraform.tfstate"
    region = "ru-central1"

    skip_credentials_validation = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    skip_s3_checksum            = true
  }
}

provider "yandex" {
  zone = "ru-central1-a"
}
