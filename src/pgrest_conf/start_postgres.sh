#!/bin/bash
export token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZGF0YV91c2VyIn0.In6_gxxxdHe_s68-CgXJNPxKDfig3S1rUGgn5geZGiQ"
echo "token exported to bash call using $token!"
docker start tutorial
./postgrest tutorial.conf
