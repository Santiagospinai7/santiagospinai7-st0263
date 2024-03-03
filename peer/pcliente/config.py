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
    return json.load(config_file)

# Inicializa la variable config con el contenido de config.json
config = load_config()
