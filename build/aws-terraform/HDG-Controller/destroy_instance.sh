#!/bin/bash

# Define log file path for Terraform destroy operation
destroy_log_file="../../logs/$(date +'%Y-%d-%m')-hdg-destroy.log"
args=("destroy" "--auto-approve") 

# Terraform destroy operation logging
{
    time (
        terraform ${args[0]} ${args[1]} 2>&1 | while IFS= read -r line; do
            printf '%s %s\n' "$(date)" "$line"
        done
    )
} 2>&1 | tee -a "$destroy_log_file" | grep real >> "$destroy_log_file"

# Define log file path for Python scraper
scraper_log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-pythonscraper.log"

# Logging related to Python scraper
echo "Please check $scraper_log_file to view any activities"

mc_details=("$(uname)" "$(lsb_release -c | awk '{print $2}')")
cat << EOF >> "$scraper_log_file"
$(printf "%0.s-" {1..32})
INFORMATION

$(printf "%0.s-" {1..32})

You are currently on $HOSTNAME
Running as user      $(whoami)
you appear to be running on ${mc_details[0]}\\${mc_details[1]}
$(printf "%0.s-" {1..32})

EOF

echo "running destroy_instance.sh" >> "$scraper_log_file"

# Finish logging for Python scraper
cat << EOF >> "$scraper_log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF
