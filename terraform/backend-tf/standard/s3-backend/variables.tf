variable "region" {
  type    = string
  default = "us-west-2"
}

variable "project" {
  description = "Name of the project"
  default     = "terraform-backend"
  type        = string
}

variable "principal_arns" {
  description = "List of principal arns allowed to assume the IAM role"
  default     = null
  type        = list(string)
}
