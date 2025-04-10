""" 
    Assign a reserved floating IP to a droplet.
    Requires the following environment variables:
    - DIGITALOCEAN_TOKEN: Your DigitalOcean API token
    - RESERVED_IP: The reserved floating IP address
    - DROPLET_NAME: The name of the droplet to assign the IP to
    Author: Wolf Paulus - https://wolfpaulus.com
"""

import os
import digitalocean
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("DIGITALOCEAN_TOKEN")
droplet_name = os.environ.get("DROPLET_NAME")
reserved_ip = os.environ.get("RESERVED_IP")

try:
    manager = digitalocean.Manager(token=token)
    my_droplets = manager.get_all_droplets()
    for d in my_droplets:
        if d.name == droplet_name:
            ip = manager.get_floating_ip(reserved_ip)
            ip.assign(d.id)
            print(f"Assigned {reserved_ip} to {d.name}")
            break
except OSError as e:
    print(f"Error: {e}")
