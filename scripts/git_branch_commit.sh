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