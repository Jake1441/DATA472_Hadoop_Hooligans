#!/bin/bash

# runs docker selenium scraper

#Test purpose go back to previous directory.
# repo=desertroam/hadoophulligans
# tag=latest
log_file="../logs/$(date +'%Y-%d-%m')-pythonscraper.log"
docker volume create scraper-db

{ time ( sudo docker compose up 2>&1 | while IFS= read -r line; do printf '%s %s\n' "$(date)" "$line"; done ); } 2>&1 | tee -a "$log_file" | grep real >> "$log_file"

#sudo docker run -it --name python-scraper $repo:$tag
