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

# helpful git script.
working_dir=$(pwd)

# set up parameters
new_commit_message='fix code execution order for github script'

# this is your branch you want to branch off, think of it like a node
current_branch=develop
git switch $current_branch

# this is the leaf branch node -> leaf node
new_branch=fix_gitscript
git branch $new_branch
git checkout $new_branch

git push origin $new_branch

# when changing need to go back to root git.
cd "$working_dir"
git add .
# git commit -m "$new_commit_message"
#git push origin $new_branch
#git switch $current_branch

# upload branch to remote
#git pull origin $new_branch

# when done
# git branch -d $new_branch

# finalise by closing out the remote branch
# git push origin -d $new_branch

log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-pythonscraper.log"
scriptfile='git_branch_commit.sh' # should be script name 

echo "Please check $log_file to view any activities"


echo "running $scriptfile" >> $log_file

#sudo docker run -it --name python-scraper $repo:$tag
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF