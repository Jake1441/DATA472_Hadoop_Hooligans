#!/bin/bash

dockerbuild='/home/ubuntu/DATA472_Hadoop_Hooligans'
dockercompose='/home/ubuntu/DATA472_Hadoop_Hooligans/build/docker-scraper'
dockerimg='desetroam/hadoophulligans:latest'

cd $dockerbuild
docker build . --no-cache -t $dockerimg

cd $dockercompose
bash start_scraper.sh

log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-docker-scraper.log"
scriptfile='rebuild_docker.sh' # should be script name 

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

# --copy below here this can be appended to end of script
#sudo docker run -it --name python-scraper $repo:$tag
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF