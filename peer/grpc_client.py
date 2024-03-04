import os
import django
import requests

import grpc
import file_management_pb2
import file_management_pb2_grpc

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peer.settings')
django.setup()

from pcliente.config import config

file_storage = []

def login():
  response = requests.post(f"{config['server_url']}login/", json=config['peer_info'])
  print(response.json())

def logout():
  response = requests.post(f"{config['server_url']}logout/", json={"username": config['peer_info']['username']})
  print(response.json())

def send_index():
  payload = config['peer_info']
  payload['files'] = file_storage 
  
  response = requests.post(f"{config['server_url']}sendIndex/", json=payload)
  print(response.json())

def query(filename):
  response = requests.get(f"{config['server_url']}query/?filename={filename}")
  print(response.json())

def grpc_upload(filename):
  with grpc.insecure_channel(f'localhost:{config["port"]}') as channel:
    stub = file_management_pb2_grpc.FileManagerStub(channel)
    response = stub.Upload(file_management_pb2.FileInfo(filename=filename))

  if response.success:
    file_storage.append(filename)
  print(f"Servidor gRPC dice: {response.message}")

def grpc_download(filename):
  with grpc.insecure_channel(f'localhost:{config["port"]}') as channel:
    stub = file_management_pb2_grpc.FileManagerStub(channel)
    try:
      response = stub.Download(file_management_pb2.FileRequest(filename=filename))
      print(f"Descargando archivo: {response.filename}")
    except grpc.RpcError as e:
      if e.code() == grpc.StatusCode.NOT_FOUND:
        print("Archivo no encontrado.")
      else:
        print(f"Error gRPC: {e.details()}")

def main():


  while True:
    print("\nOpciones:")
    print("1. Login")
    print("2. Logout")
    print("3. Send Index")
    print("4. Query")
    print("5. Upload")
    print("6. Download")
    print("7. Exit")

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
      filename = input("Ingrese el nombre del archivo para subir: ")
      grpc_upload(filename)
    elif choice == '6':
      filename = input("Ingrese el nombre del archivo para descargar: ")
      grpc_download(filename)
    elif choice == '7':
      print("Saliendo...")
      break
    else:
      print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == '__main__':
    main()
