# see roles from postgres
SELECT rolname from pg_roles;
- drop a role
drop role <role_name>;
If this does not work try the following
REASSIGN OWNED BY <role_name> TO postgres;
DROP OWNED BY <role_name>;
drop role <role_name>;
SELECT rolname from pg_roles;
confirm <role_name> does not exist.

# examples
The examples provided use bash scripts and curl. 

the code is provided to post, update and view specific sets of data.
there is code to view the entire table and code to show how to do a multiline post.

most of the lines are provided and can be run to reproduce your desired database but
you will require some copy/pasting of secret keys from jwt.io whilst most of the rest is done by
the script. 

You will need to make sure you have postgres running the configuration file as well as having the docker set up the steps are as follows.

# test schema create
1. Stop the Docker container named "tutorial".
2. Remove all Docker containers.
3. Create a new PostgreSQL Docker container named "tutorial" with the following configurations:
    - Name: tutorial
    - Port mapping: 5433 to 5432
    - Environment variable: POSTGRES_PASSWORD=mysecretpassword
4. Execute PostgreSQL commands inside the Docker container to:
    - Drop existing table and schema
    - Create a new schema
    - Create a new table with columns (id, obs_value, measure_unit, obs_timestamp)
5. Insert data into the created table inside the Docker container.
6. Create a role named <your_web_service> for web access with the following permissions:
    - Grant usage on schema <db>
    - Grant select on <db>.<tbl>
    - Create another role named "authenticator" with login and grant <your_web_service> to it.
7. Create a role named <your_user> for manipulating data using CURL with the following permissions:
    - Grant <your_user> to authenticator
    - Grant usage on schema <db>
    - Grant all on <db>.<tbl>
    - Grant usage, select on sequence <db>.<tbl>_id_seq
8. Create a secret key file named "tutorial.conf" with a randomly generated JWT secret (commented out).
9. Output the contents of "tutorial.conf" (commented out).
10. Generate a secret key using jwt.io with the following settings:
    - Header: {"alg": "HS256", "typ": "JWT"}
    - Payload: {"role": "username"}
11. Replace "your-256-bit-secret" with the password from "tutorial.conf" in the JWT payload.
12. Copy the generated JWT token and replace the TOKEN variable inside "test_curl_post.sh".
13. Uncomment the line to run postgrest with the configuration file "tutorial.conf".

# test curl post
1. Export the TOKEN variable from step 12.
2. Send a POST request to the localhost endpoint with JSON data containing "measure_unit" and "obs_value" fields:
    - Endpoint: http://localhost:3000/<tbl>
    - Headers:
        - Authorization: Bearer $TOKEN
        - Content-Type: application/json
    - Data:
        ```json
        {
            "measure_unit": "grams",
            "obs_value": "100"
        }
        ```
3. Send a GET request to the localhost endpoint to check changes in the table:
    - Endpoint: http://localhost:3000/<tbl>
4. Send a PATCH request to update data in the table with the specified ID:
    - Endpoint: http://localhost:3000/<tbl>?id=eq.2
    - Headers:
        - Authorization: Bearer $TOKEN
        - Content-Type: application/json
    - Data:
        ```json
        {
            "obs_value": "20"
        }
        ```
5. Send a POST request with multi-line data to the localhost endpoint:
    - Endpoint: http://localhost:3000/<tbl>
    - Headers:
        - Authorization: Bearer $TOKEN
        - Content-Type: application/json
    - Data:
        ```json
        {
            "measure_unit": "USD",
            "obs_value": "10.5"
        }
        ```
6. Query the database using a GET request with specific parameters:
    - Endpoint: http://localhost:3000/<tbl>
    - Query Parameters:
        - select=obs_value,obs_timestamp
        - measure_unit=eq.USD
