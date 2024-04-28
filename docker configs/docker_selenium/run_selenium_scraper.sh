#!/bin/bash

# runs docker selenium scraper
# fname is the file name.

# name of the image is selenium-headless-d472
# the docker container name is selcontainer

fname="getcontent.py"
docker rmi selenium-headless-d472
docker build . -t selenium-headless-d472
docker run -d --name selcontainer selenium-headless-d472
docker cp $fname selcontainer:/python_scrape
docker exec -it selcontainer python $fname
# copy file out of docker container (may need to be a for loop if theres multiple files as not tested!)
docker cp selcontainer:/python_scrape/$(docker exec -i selcontainer find . -name *.xlsx | sed 's/^.\///') .
# stop container and remove.
docker stop selcontainer
docker rm selcontainer
