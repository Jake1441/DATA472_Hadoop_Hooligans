#!/bin/bash

find . -type f -not -path '*/\.git/*' -exec grep -l 'run_docker_scraper.sh' {} \; -exec sed -i 's/run_docker_scraper.sh/start_scraper.sh/g' {} \;

log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-pythonscraper.log"
scriptfile='find_rename.sh' # should be script name 

echo "Please check $log_file to view any activities"

mc_details=("$(uname)" "$(lsb_release -c | awk '{print $2}')")
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
INFORMATION

$(printf "%0.s-" {1..32})

You are currently on $HOSTNAME
Running as user      $(whoami)
you appear to be running on ${mc_details[0]}\\${mc_details[1]}
$(printf "%0.s-" {1..32})

EOF


echo "running $scriptfile" >> $log_file

#sudo docker run -it --name python-scraper $repo:$tag
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF