#!/bin/bash

# set up env script
touch .env
# build the required packages
sh ./scripts/setup_ansible_mini.sh
sh ./scripts/init_ansible.sh