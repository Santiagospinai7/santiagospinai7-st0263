import json

STORAGE_FILE_PATH = 'files_storage.json'

def load_files_storage():
  try:
    with open(STORAGE_FILE_PATH, 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_files_storage(files_storage):
  with open(STORAGE_FILE_PATH, 'w') as file:
    json.dump(files_storage, file)
