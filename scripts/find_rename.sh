find . -type f -not -path '*/\.git/*' -exec grep -l 'run_docker_scraper.sh' {} \; -exec sed -i 's/run_docker_scraper.sh/start_scraper.sh/g' {} \;
