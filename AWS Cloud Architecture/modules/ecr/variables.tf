variable "ecr_name" {
  description = "The name of the ECR repository"
  type = string
  default     = "titanic-image"
}

variable "image_mutability" {
  description = "image mutability"
  type        = string
  default     = "IMMUTABLE"
}
