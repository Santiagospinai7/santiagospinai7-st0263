import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peer.settings')
django.setup()

from pcliente.config import config

files_storage = []

def login():
  response = requests.post(f"{config['server_url']}login/", json=config['peer_info'])
  print(response.json())

def logout():
  response = requests.post(f"{config['server_url']}logout/", json={"username": config['peer_info']['username']})
  print(response.json())

def send_index():
  # Asume que config['peer_info'] ya está configurado correctamente
  payload = config['peer_info']
  payload['files'] = files_storage  # Envía la lista simulada de archivos
  
  # Envía el índice de archivos al servidor central
  response = requests.post(f"{config['server_url']}sendIndex/", json=payload)
  print(response.json())

def query(filename):
  response = requests.get(f"{config['server_url']}query/?filename={filename}")
  print(response.json())

def main():
  while True:
    print("\nOpciones:")
    print("1. Login")
    print("2. Logout")
    print("3. Send Index")
    print("4. Query")
    print("5. Exit")
    choice = input("Seleccione una opción: ")

    if choice == '1':
      login()
    elif choice == '2':
      logout()
    elif choice == '3':
      send_index()
    elif choice == '4':
      filename = input("Ingrese el nombre del archivo para buscar: ")
      query(filename)
    elif choice == '5':
      print("Saliendo...")
      break
    else:
      print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    main()
