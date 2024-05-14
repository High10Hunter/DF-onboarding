provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "terraform-bucket" {
  bucket = "terraform-bucket-h10h-update"

  tags = {
    Name        = "Terraform Series"
  }
}