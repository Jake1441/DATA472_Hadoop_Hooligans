dockerbuild='/home/ubuntu/DATA472_Hadoop_Hooligans'
dockercompose='/home/ubuntu/DATA472_Hadoop_Hooligans/build/docker_selenium'
dockerimg='desetroam/hadoophulligans:latest'

cd $dockerbuild
docker build . --no-cache -t $dockerimg

cd $dockercompose
bash start_scraper.sh