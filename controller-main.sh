
cd ./build/docker_selenium/
sh run_docker_scraper.sh
sudo apt install -y python3.12-venv
alias activate=". ~/.venv/bin/activate"
python3 -m venv ~/.venv && activate
pip install docker
ls -lla
# python3 exportdata.py
# deactivate