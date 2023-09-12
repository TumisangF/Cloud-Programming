terraform {
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 4.24.0"
      }
    }
}

provider "aws" {
    region = var.aws_region
}

module "ecr-repo" {
    source = "./../modules/ecr"
}

module "ec2-instance" {
    source = "./../modules/ec2"
}
