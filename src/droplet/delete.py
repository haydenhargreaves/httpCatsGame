""" 
    Deletes a droplet from Digital Ocean 
    Requires the following environment variables:
    - DIGITALOCEAN_TOKEN: Your DigitalOcean API token
    - DROPLET_NAME: The name of the droplet to delete
    Author: Wolf Paulus - https://wolfpaulus.com    
"""

import os
import digitalocean
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("DIGITALOCEAN_TOKEN")
droplet_name = os.environ.get("DROPLET_NAME")

for droplet in digitalocean.Manager(token=token).get_all_droplets():
    if droplet.name == droplet_name:
        droplet.destroy()
        print("Droplet destroyed")
        break
