variable "ec2_ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0c147c2e2b026f094"
}

variable "ec2_instance_type" {
  description = "Instance type for the EC2 instance"
  type        = string
  default     = "t3.micro"
}

variable "ec2_subnet_id" {
  description = "Subnet ID for the EC2 instance"
  type        = string
  default     = "subnet-0cee1f69b6dfa19d9"
}

variable "ec2_key_name" {
  description = "Key name for SSH access"
  type        = string
  default     = "titanic key"
}

variable "ec2_instance_name" {
  description = "Name for the EC2 instance"
  type        = string
  default     = "titanic instance"
}

variable "ec2_environment" {
  description = "Environment tag for the EC2 instance"
  type        = string
  default     = "Dev"
}

variable "security_group_id" {
  description = "The ID of the security group to associate with the EC2 instance"
  type        = string
  default     = "sg-033fdd1beed3d756e"
}

