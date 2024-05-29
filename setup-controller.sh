#!/bin/bash

# set up env script
touch .env
# build the required packages
sh ./scripts/setup_ansible_mini.sh
sh ./scripts/init_ansible.sh
if ! getent group docker; then sudo groupadd docker; fi
sudo usermod -aG docker ubuntu
sudo systemctl enable docker
sudo systemctl restart docker