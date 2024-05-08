import jwt
import json

# make sure its pyjwt not jwt!

config_file = open('db_params.json', )
data = json.load(config_file)
print(data["role"])



# Your secret key, keep this secure

# TODO: open tutorial.conf and get the key (usually the last line).
# get the role for the user accessing the data as well where that is stored i.e data_user is used so string that contains this first might be the best to use.
# create the key, save it for use

# open tutorial.conf
#secret_key = 'JvJ5XuVlhe9RdkXU7nzzmhIpraYXwyDf'
secret_key = data["jwt_secret"]

# Payload data for the token
payload = {
    'role': data["role"]  # ,
    # this isn't used in the jwt.io probably because its just a developer token
    # 'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1)  # Token expiration time
}

# Create the JWT token
token = jwt.encode(payload, secret_key, algorithm='HS256')
data = f"""#!/bin/bash
export token="{token}"
echo "token exported to bash call using $token!"
docker start tutorial
./postgrest tutorial.conf
"""
with open("start_postgres.sh", "w") as file:
    file.write(data)

print(token)

#script_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZGF0YV91c2VyIn0.wtvgPKgvVPMa0QqbVd2D9TllPOX6C-lTq44l66FhSdM"

# save the key
