#!/bin/bash

# build the required packages
sh ./scripts/setup_ansible_mini.sh
sh ./init_ansible.sh
pip install -y docker
