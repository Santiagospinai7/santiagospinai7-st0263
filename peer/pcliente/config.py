# import json

# def load_config():
#   with open('config.json', 'r') as config_file:
#     return json.load(config_file)

# aconfig = load_config()


import json
import os
from django.conf import settings

def load_config():
  config_path = os.path.join(settings.BASE_DIR, 'pcliente', 'config.json')
  with open(config_path, 'r') as config_file:
      config = json.load(config_file)
  
  ip = config.get('ip', '127.0.0.1') 
  port = config.get('port', 8001)
  url = f"http://{ip}:{port}"
  
  # Actualizar la URL en peer_info
  config['peer_info']['url'] = url

  return config

config = load_config()
