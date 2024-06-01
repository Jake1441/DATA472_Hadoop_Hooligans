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
drop table <db>.<tbl>;
drop schema <db>;

create schema <db>;

create table <db>.<tbl> (
  id serial primary key,
  obs_value numeric not null default 0,
  measure_unit text not null,
  obs_timestamp timestamptz
);
\q
EOF

# old code.
# insert into <db>.<tbl> (task) values
# ('finish tutorial 0'), ('pat self on back');

# each not null field or any field you need to add data has to be specified i.e
# insert into (measurement_unit, value, quantity) values

# example of adding multiple values each different row will be separated as above! i.e
# ('grams', '100', '3'), ('usd', '100',1);
cat << EOF | sudo docker exec -i tutorial psql -U postgres 
insert into <db>.<tbl> (measure_unit,obs_value) values
  ('grams', '100');
\q
EOF

# creating web access role for the tutorial configuration.
cat << EOF | sudo docker exec -i tutorial psql -U postgres 
create role <your_web_service> nologin;

grant usage on schema <db> to <your_web_service>;
grant select on <db>.<tbl> to <your_web_service>;

create role authenticator noinherit login password 'mysecretpassword';
grant <your_web_service> to authenticator;
EOF

# creating the user who will manipulate the data using CURL
cat << EOF | sudo docker exec -i tutorial psql -U postgres 
create role <your_user> nologin;
grant <your_user> to authenticator;

grant usage on schema <db> to <your_user>;
grant all on <db>.<tbl> to <your_user>;
grant usage, select on sequence <db>.<tbl>_id_seq to <your_user>;
\q
EOF

# note this secret is not designed for production machines.

# creating tutorial file
#uncomment the bash code to run.

# Allow "tr" to process non-utf8 byte sequences
#export LC_CTYPE=C

# read random bytes and keep only alphanumerics
#echo "jwt-secret = \"$(LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c32)\"" >> tutorial.conf

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
# remeber to replace your-256-bit-secret with the password in tutorial.conf

# copy all of the code to the left and place it in the TOKEN variable located inside test_curl_post.sh

# Running postgrest installed from a package manager
# when happy uncomment this line below.
# postgrest tutorial.conf

# I copied these over
log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-pythonscraper.log"
scriptfile='test_schema_create.sh' # should be script name 

echo "Please check $log_file to view any activities"


echo "running $scriptfile" >> $log_file

# Copied this over
#sudo docker run -it --name python-scraper $repo:$tag
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF