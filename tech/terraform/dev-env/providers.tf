terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["C:\\Users\\jacob\\.aws\\credentials"]
  profile                  = "1P-VsCode-Terraform"
}