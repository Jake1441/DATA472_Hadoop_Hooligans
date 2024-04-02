 #!/bin/bash
 #measure_unit,obs_value
 
 # if this doesnt work make sure the role in jwt matched the role you chose for the user accessing the tale!
 
export TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZGF0YV91c2VyIn0.4HFMI2Rnen8KvNbmKzkO8y9hraTDzqf0s1QWE4wzHDg"
curl http://localhost:3000/data -X POST \
     -H "Authorization: Bearer $TOKEN"   \
     -H "Content-Type: application/json" \
     -d '{"measure_unit": "grams", "obs_value": "100"}'
# check changes
curl http://localhost:3000/data

# update 
curl http://localhost:3000/data?id=eq.2 -X PATCH \
     -H "Authorization: Bearer $TOKEN"   \
     -H "Content-Type: application/json" \
     -d '{"obs_value" : "20"}'

# additional code, multi-line use.

curl "http://localhost:3000/data" \
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
curl "http://localhost:3000/data?select=obs_value,obs_timestamp&measure_unit=eq.USD"