import jwt
# make sure its pyjwt not jwt!

# Your secret key, keep this secure

# TODO: open tutorial.conf and get the key (usually the last line).
# get the role for the user accessing the data as well where that is stored i.e data_user is used so string that contains this first might be the best to use.
# create the key, save it for use

# open tutorial.conf
secret_key = 'JvJ5XuVlhe9RdkXU7nzzmhIpraYXwyDf'

# Payload data for the token
payload = {
    'role': "data_user"  # ,
    # this isn't used in the jwt.io probably because its just a developer token
    # 'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=1)  # Token expiration time
}

# Create the JWT token
token = jwt.encode(payload, secret_key, algorithm='HS256')
print(token)

script_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZGF0YV91c2VyIn0.wtvgPKgvVPMa0QqbVd2D9TllPOX6C-lTq44l66FhSdM"

# save the key
