#!/bin/bash

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

dockerbuild='/home/ubuntu/DATA472_Hadoop_Hooligans'
dockercompose='/home/ubuntu/DATA472_Hadoop_Hooligans/build/docker-scraper'
dockerimg='desetroam/hadoophulligans:latest'

cd $dockerbuild

{ time ( docker build . --no-cache -t $dockerimg | while IFS= read -r line; do printf '%s %s %s %s %s\n' "$HOSTNAME:" "$(whoami)" - "$(date)" "$line"; done ); } 2>&1 | tee -a "$log_file" | grep real >> "$log_file"
# note the {time (cmd plus args | while IFS= read -r line; do printf '%s %s %s %s %s\n' "$HOSTNAME:" "$(whoami)" - "$(date)" "$line"; done ); } 2>&1 | tee -a "$log_file" | grep real >> "$log_file")}
# Thats the part that outputs to the logs :) Eventually we can use an environment variable to make it easier.

cd $dockercompose
bash start_scraper.sh

log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-docker-scraper.log"
scriptfile='rebuild_docker.sh' # should be script name 

echo "Please check $log_file to view any activities"


echo "running $scriptfile" >> $log_file

# --copy below here this can be appended to end of script
#sudo docker run -it --name python-scraper $repo:$tag
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF