# helpful git script.

# set up parameters
new_commit_message="added script for github branching"

# this is your branch you want to branch off, think of it like a node
current_branch=develop
# this is the leaf branch node -> leaf node
new_branch=target_branch
git branch $new_branch
git checkout $new_branch
git add .
# git commit -m "$new_commit_message"

#git switch $current_branch
#git pull origin $new_branch
#git push origin $current_branch

# when done
# git branch -d $new_branch