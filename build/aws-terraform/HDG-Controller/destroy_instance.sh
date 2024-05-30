#!/usr/bin/env bash

log_file="../../logs/$(date +'%Y-%d-%m')-hdg-destroy.log"
args=("destroy" "--auto-approve") 

{
    time (
        terraform ${args[0]} ${args[1]} 2>&1 | while IFS= read -r line; do
            printf '%s %s\n' "$(date)" "$line"
        done
    )
} 2>&1 | tee -a "$log_file" | grep real >> "$log_file"