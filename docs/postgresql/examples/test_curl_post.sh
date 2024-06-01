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

#measure_unit,obs_value
 
# if this doesnt work make sure the role in jwt matched the role you chose for the user accessing the tale!
 
export TOKEN=""
curl http://localhost:3000/<tbl> -X POST \
     -H "Authorization: Bearer $TOKEN"   \
     -H "Content-Type: application/json" \
     -d '{"measure_unit": "grams", "obs_value": "100"}'
# check changes
curl http://localhost:3000/<tbl>

# update 
curl http://localhost:3000/<tbl>?id=eq.2 -X PATCH \
     -H "Authorization: Bearer $TOKEN"   \
     -H "Content-Type: application/json" \
     -d '{"obs_value" : "20"}'

# additional code, multi-line use.

curl "http://localhost:3000/<tbl>" \
  -X POST \
  -H "Authorization: Bearer $TOKEN"   \
  -H "Content-Type: application/json" \
  -d @- << EOF
  {
    "measure_unit": "USD",
    "obs_value": "10.5"
  }
EOF

# query the database
curl "http://localhost:3000/<tbl>?select=obs_value,obs_timestamp&measure_unit=eq.USD"

# I copied these over
log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-pythonscraper.log"
scriptfile='test_curl_post.sh' # should be script name 

echo "Please check $log_file to view any activities"


echo "running $scriptfile" >> $log_file

# Copied this over
#sudo docker run -it --name python-scraper $repo:$tag
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF