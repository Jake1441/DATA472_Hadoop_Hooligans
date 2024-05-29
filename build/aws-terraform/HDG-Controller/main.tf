provider "aws" {
  region = var.region
}

resource "aws_instance" "DATA472-jre141-ubuntu_instance" {
  ami                         = var.ami
  instance_type               = var.instance_type
  subnet_id                   = var.subnetid
  vpc_security_group_ids      = var.vpc_security_group_ids
  associate_public_ip_address = true
  key_name                    = var.instance_keypair_name
  ebs_optimized               = false
  tags = {
    Name     = var.name
    Course   = var.course
    UserName = var.username
  }
  ebs_block_device {
    device_name = "/dev/sda1"
    volume_size = var.volumesize
  }
  volume_tags = {
    Name     = var.name
    Course   = var.course
    UserName = var.username
  }


}
# you will need to put your private_key path.

resource "null_resource" "build_git_repo" {
  connection {
    type        = "ssh"
    user        = "ubuntu"
    host        = aws_instance.DATA472-jre141-hadoop-instance.public_ip
    private_key = file("//mnt//c//Users//jacob//Downloads//DATA472-jre141-2.pem")
  }
  provisioner "remote-exec" {
    inline = [
      "echo 'Hello from Terraform ${timestamp()}'",
      "sudo apt update",
      "sudo apt install -y git",
      "git clone -b ${var.git_branch} ${var.git_repo} ${var.git_repo_dir}",
      "cd ${var.git_repo_dir} && git pull origin ${var.git_branch}",
      "echo ls -lla",
	  "cd /home/ubuntu/${var.git_repo_dir}",
	  "sh main.sh",
      "cd /home/ubuntu/${var.git_repo_dir}/build/docker_selenium",
      "sudo sh run_docker_scraper.sh"
    ]
  }
}

output "ec2_global_ips" {
  value = aws_instance.DATA472-jre141-hadoop-instance.*.public_ip
}