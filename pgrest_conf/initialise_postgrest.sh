#!/bin/bash

# postgres uses semicolons ';' to finish each line
# in bash the \ represents this is a multi-line code but to run all as one line.
# sudo is running as highly priviledged user, 
# docker does not have sudo and runs always as high priviledges!

# basic admin stuff, assuming you had named your docker container tutorial, if not rename both
# this and the next line sudo docker run --name tutorial to the preferred name of your container.
# did you check that tutorial was not named after another container you had?

docker stop tutorial
# this command should only be run if you are confident you don't care about other stopped containers being deleted!
# docker ps -aq shows all containers but only ids. docker ps -a usually only shows running containers.
docker rm $(docker ps -aq)


# this command creates the tutorial posgres docker
sudo docker run --name tutorial -p 5433:5432 \
                -e POSTGRES_PASSWORD=mysecretpassword \
                -d postgres


#  sudo docker exec -ti tutorial psql -U postgres 
# test create schema
cat << EOF | sudo docker exec -i tutorial psql -U postgres 
drop table datab1.data;
drop schema datab1;

create schema datab1;

create table datab1.data (
  id serial primary key,
  obs_value numeric not null default 0,
  measure_unit text not null,
  obs_timestamp timestamptz
);
\q
EOF

# old code.
# insert into datab1.data (task) values
# ('finish tutorial 0'), ('pat self on back');

# each not null field or any field you need to add data has to be specified i.e
# insert into (measurement_unit, value, quantity) values

# example of adding multiple values each different row will be separated as above! i.e
# ('grams', '100', '3'), ('usd', '100',1);
cat << EOF | sudo docker exec -i tutorial psql -U postgres 
insert into datab1.data (measure_unit,obs_value) values
  ('grams', '100');
\q
EOF

# creating web access role for the tutorial configuration.
cat << EOF | sudo docker exec -i tutorial psql -U postgres 
create role web_dbaccess nologin;

grant usage on schema datab1 to web_dbaccess;
grant select on datab1.data to web_dbaccess;

create role authenticator noinherit login password 'mysecretpassword';
grant web_dbaccess to authenticator;
EOF

# creating the user who will manipulate the data using CURL
# this role is used by JWT.
cat << EOF | sudo docker exec -i tutorial psql -U postgres 
create role data_user nologin;
grant data_user to authenticator;

grant usage on schema datab1 to data_user;
grant all on datab1.data to data_user;
grant usage, select on sequence datab1.data_id_seq to data_user;
\q
EOF

# note this secret is not designed for production machines.

# creating tutorial file
#uncomment the bash code to run.

# Allow "tr" to process non-utf8 byte sequences
export LC_CTYPE=C

# read random bytes and keep only alphanumerics
echo 'db-uri = "postgres://authenticator:mysecretpassword@localhost:5433/postgres"' > tutorial.conf
echo 'db-schemas = "datab1"' >> tutorial.conf
echo 'db-anon-role = "web_dbaccess"' >> tutorial.conf
echo "jwt-secret = \"$(LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c32)\"" >> tutorial.conf

# PASSWORD MUST BE AT LEAST 32 CHARS LONG
#cat tutorial.conf

# use jwt.io to create a secret key for test_curl_post.sh

# jwt.io
# header
# {
#   "alg": "HS256",
#   "typ": "JWT"
# }
# payload
# {
#   "role": "username",
# }
# ie 

# { 
# 	"role": "data_user",
# }

# remeber to replace your-256-bit-secret with the password in tutorial.conf

# copy all of the code to the left and place it in the TOKEN variable located inside test_curl_post.sh

# Running postgrest installed from a package manager
# when happy uncomment this line below.
# postgrest tutorial.conf
sh start_postgres.sh