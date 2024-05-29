#!/bin/bash

# build the required packages
sh ./scripts/setup_ansible_mini.sh
sh ./scripts/init_ansible.sh
pip install docker

cd ./build/docker_selenium/
sh run_docker_scraper.sh
python exportdata.py