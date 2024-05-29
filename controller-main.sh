
cd ./build/docker_selenium/
sh run_docker_scraper.sh
sudo apt install -y python3.12-venv
python3 -m venv ~/.venv && source ~/.venv/bin/activate
python3 exportdata.py
deactivate