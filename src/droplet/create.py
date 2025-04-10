""" 
    Create a DigitalOcean droplet using the DigitalOcean API 
    Requires the following environment variables:
    - DIGITALOCEAN_TOKEN: Your DigitalOcean API token
    - DROPLET_NAME: The name of the droplet to create
    - SSH_KEY: The SSH key to use for the droplet
    Author: Wolf Paulus - https://wolfpaulus.com
"""

import os
import digitalocean
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("DIGITALOCEAN_TOKEN")
droplet_name = os.environ.get("DROPLET_NAME")

droplet_args = {
    "name": droplet_name,  # Name of the droplet
    "region": "sfo3",  # San Francisco 3
    "image": "ubuntu-24-04-x64",  # Ubuntu 24.04 (LTS) x64
    "size_slug": "s-1vcpu-512mb-10gb",  # 512 MB RAM, 1 vCPU, 10 GB SSD
    "ipv6": False,
    "backups": False,
    "tags": ["iac"],
}

try:
    manager = digitalocean.Manager(token=token)
    my_droplets = manager.get_all_droplets()
    if droplet_args["name"] in [d.name for d in my_droplets]:
        print("Droplet already exists")
        exit()
    digitalocean.Droplet(
        token=token, ssh_keys=manager.get_all_sshkeys(), **droplet_args
    ).create()
    print("Droplet created ... wait a few seconds before assigning an IP")
except OSError as e:
    print(f"Error: {e}")
