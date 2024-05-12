#!/bin/bash

# postgres uses semicolons ';' to finish each line
# in bash the \ represents this is a multi-line code but to run all as one line.
# sudo is running as highly priviledged user,
# docker does not have sudo and runs always as high priviledges!

# basic admin stuff, assuming you had named your docker container tutorial, if not rename both
# this and the next line sudo docker run --name tutorial to the preferred name of your container.
# did you check that tutorial was not named after another container you had?

# collect postgrest application
wget https://github.com/PostgREST/postgrest/releases/download/v12.0.2/postgrest-v12.0.2-linux-static-x64.tar.xz postgrest-v12.0.2-linux-static-x64.tar.xz
tar xJf postgrest-v12.0.2-linux-static-x64.tar.xz

docker stop tutorial
# this command should only be run if you are confident you don't care about other stopped containers being deleted!
# docker ps -aq shows all containers but only ids. docker ps -a usually only shows running containers.
docker rm $(docker ps -aq)
database_user=data_user

# this command creates the tutorial posgres docker
sudo docker run --name tutorial -p 5433:5432 \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -d postgres

sleep 5s
#  sudo docker exec -ti tutorial psql -U postgres
# test create schema
cat <<EOF | sudo docker exec -i tutorial psql -U postgres
drop table datab1.data;
drop schema datab1;

create schema datab1;

create table datab1.data (
  id serial primary key,
  obs_value numeric not null default 0,
  date timestamp,
  Unit numeric not null default 0,
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
cat <<EOF | sudo docker exec -i tutorial psql -U postgres
insert into datab1.data (measure_unit,obs_value) values
  ('grams', '100');
\q
EOF

# creating web access role for the tutorial configuration.
cat <<EOF | sudo docker exec -i tutorial psql -U postgres
create role web_dbaccess nologin;

grant usage on schema datab1 to web_dbaccess;
grant select on datab1.data to web_dbaccess;

create role authenticator noinherit login password 'mysecretpassword';
grant web_dbaccess to authenticator;
EOF

# creating the user who will manipulate the data using CURL
# this role is used by JWT. Payload { "role" : "data_user" }
cat <<EOF | sudo docker exec -i tutorial psql -U postgres
create role $database_user nologin;
grant $database_user to authenticator;

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
echo 'db-anon-role = "web_dbaccess"' >>tutorial.conf
jwt_secret_code=$(LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c32)
echo "jwt-secret = " "$jwt_secret_code" >> tutorial.conf

JSON_STRING=$( jq -n \
                  --arg urole "$database_user" \
                  --arg jwts "$jwt_secret_code" \
                  '{role: $urole, jwt_secret: $jwts}' )

echo "$JSON_STRING" > db_params.json

source start_postgres.sh
