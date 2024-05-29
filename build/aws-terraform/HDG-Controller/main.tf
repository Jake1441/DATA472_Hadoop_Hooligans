provider "aws" {
  region = var.region
}

resource "aws_instance" "DATA472-jre141-hdg-controller" {
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
    host        = aws_instance.DATA472-jre141-hdg-controller.public_ip
    private_key = file("//mnt//c//Users//jacob//Downloads//DATA472-jre141-2.pem")
  }
  provisioner "remote-exec" {
    inline = [
      "echo 'AWS EC2 CONTROLLER ${var.instance_type}'",
      "echo 'Initial configuration ${timestamp()}'",
      "sudo apt update",
      "sudo apt install -y git",
      "sudo rm -rf  ${var.git_repo_dir}",
      "git clone -b ${var.git_branch} ${var.git_repo} ${var.git_repo_dir}",
      "cd ${var.git_repo_dir} && git pull origin ${var.git_branch}",
      "ls -lla",
      "cd /home/ubuntu/${var.git_repo_dir}",
      "sh setup-controller.sh"
    ]
  }
}

resource "null_resource" "docker_credentials" {
  connection {
    type        = "ssh"
    user        = "ubuntu"
    host        = aws_instance.DATA472-jre141-hdg-controller.public_ip
    private_key = file("//mnt//c//Users//jacob//Downloads//DATA472-jre141-2.pem")
  }
  provisioner "remote-exec" {
    inline = [
      "echo 'AWS EC2 CONTROLLER ${var.instance_type}'",
      "echo 'Configuring docker permissions ${timestamp()}'",
      "sudo usermod -aG docker $USER"
    ]
  }
}

resource "null_resource" "resume_configuration" {
  connection {
    type        = "ssh"
    user        = "ubuntu"
    host        = aws_instance.DATA472-jre141-hdg-controller.public_ip
    private_key = file("//mnt//c//Users//jacob//Downloads//DATA472-jre141-2.pem")
  }
  provisioner "remote-exec" {
    inline = [
      "echo 'AWS EC2 CONTROLLER ${var.instance_type}'",
      "echo 'Resuming Configuration ${timestamp()}'",
      "sh controller-main.sh"
    ]
  }
}

output "ec2_global_ips" {
  value = aws_instance.DATA472-jre141-hdg-controller.*.public_ip
}

output "ec2_instance_finished" {
  value = "Done \n please set up .env under ${var.git_repo_dir} and then run the database script"
}