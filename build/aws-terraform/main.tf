terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_instance" "DATA472-jre141-ubuntu_instance" {
  ami                         = "ami-080660c9757080771"
  instance_type               = "t2.micro"
  subnet_id                   = "subnet-0326da008b859395c"
  vpc_security_group_ids      = ["sg-09b486a14a006c62b"]
  associate_public_ip_address = true
  key_name                    = "DATA472-jre141-2"
  ebs_optimized               = false
  tags = {
    Name     = var.name
    Course   = var.course
    UserName = var.username
  }
  ebs_block_device {
    device_name = "/dev/sda1"
    volume_size = 20
  }
  volume_tags = {
    Name     = var.name
    Course   = var.course
    UserName = var.username
  }


}

# resource "aws_ebs_volume" "ebs_volume" {
#   availability_zone = "ap-southeast-2b"
#   size              = 20
#   type              = "gp3"
#   iops              = 3000
#   throughput        = 125
#   encrypted         = false
#   tags = {
#     Name     = var.name
#     Course   = var.course
#     UserName = var.username
#   }

# }