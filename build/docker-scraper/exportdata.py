import os
import shutil
import docker

# Configuration
target_container = "python-scraper"
dest_dir = "automated_download_script"
container_dir = "/app/well_data"

# Initialize Docker client
client = docker.from_env()

def docker_copy(local_dir, target_container, container_dir):
    try:
        container = client.containers.get(target_container)
        tar_stream, _ = container.get_archive(container_dir)
        
        # Extract the tar stream to the destination directory
        with open('/tmp/archive.tar', 'wb') as f:
            for chunk in tar_stream:
                f.write(chunk)
        
        shutil.unpack_archive('/tmp/archive.tar', local_dir)
        os.remove('/tmp/archive.tar')
        
        print(f"Copy successful. Listing contents of {local_dir}:")
        for root, dirs, files in os.walk(local_dir):
            for name in files:
                print(os.path.join(root, name))
        return True
    except Exception as e:
        print(f"Error: Failed to copy directory from container. {e}")
        return False

def is_svn():
    dir = os.getcwd()
    while dir != "/":
        if os.path.isdir(os.path.join(dir, dest_dir)):
            if docker_copy(os.path.join(dir, dest_dir), target_container, container_dir):
                return True
        dir = os.path.dirname(dir)
    return False

if __name__ == "__main__":
    if is_svn():
        print(f"{dest_dir} directory found!")
    else:
        print(f"{dest_dir} directory not found.")
        print(f"Creating {dest_dir} directory!")
        
        new_dir = os.path.abspath(os.path.join(os.getcwd(), "../../", dest_dir))
        os.makedirs(new_dir, exist_ok=True)
        
        if is_svn():
            print(f"{dest_dir} directory created and found!")
        else:
            print(f"Failed to find or create {dest_dir} directory.")
