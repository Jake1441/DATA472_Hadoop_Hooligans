#!/bin/bash

# runs docker selenium scraper
# fname is the file name.

# name of the image is selenium-headless-d472
# the docker container name is selcontainer

#docker rmi selenium-headless-d472
#docker build . -t selenium-headless-d472

# test running
# stage 1 - Ecan

#Test purpose go back to previous directory.
repo=desertroam/hadoophulligans
tag=python

docker run -it --name python-scraper $repo:$tag
