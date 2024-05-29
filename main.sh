#!/bin/bash

# build the required packages
sh ./scripts/setup_ansible_mini.sh
sh ./scripts/init_ansible.sh
sudo mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3.12/EXTERNALLY-MANAGED.old
pip install docker
sudo mv /usr/lib/python3.12/EXTERNALLY-MANAGED.old /usr/lib/python3.12/EXTERNALLY-MANAGED

cd ./build/docker_selenium/
sh run_docker_scraper.sh
python exportdata.py