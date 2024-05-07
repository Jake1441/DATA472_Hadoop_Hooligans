# helpful git script.
working_dir=$(pwd)

# set up parameters
new_commit_message='update github script for branching'

# this is your branch you want to branch off, think of it like a node
current_branch=develop
git switch $current_branch

# this is the leaf branch node -> leaf node
new_branch=git_script_fix_adding
git branch $new_branch
git checkout $new_branch

# when changing need to go back to root git.

cd "$working_dir"
git add .
# git commit -m "$new_commit_message"

#git switch $current_branch

#git push origin $current_branch
#git pull origin $new_branch

# when done
# git branch -d $new_branch