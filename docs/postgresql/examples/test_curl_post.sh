 #!/bin/bash
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