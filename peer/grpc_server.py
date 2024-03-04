from concurrent import futures
import grpc
import file_management_pb2
import file_management_pb2_grpc

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peer.settings')
django.setup()

from pcliente.config import config

files_storage = []

class FileManagerServicer(file_management_pb2_grpc.FileManagerServicer):
  def Upload(self, request, context):
    filename = request.filename
    if filename not in files_storage:
      files_storage.append(filename)
      return file_management_pb2.FileResponse(success=True, message="Archivo subido exitosamente.")
    else:
      return file_management_pb2.FileResponse(success=False, message="El archivo ya existe.")

  def Download(self, request, context):
    filename = request.filename
    if filename in files_storage:
      return file_management_pb2.FileInfo(filename=filename)
    else:
      context.abort(grpc.StatusCode.NOT_FOUND, "Archivo no encontrado")

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  file_management_pb2_grpc.add_FileManagerServicer_to_server(FileManagerServicer(), server)
  server.add_insecure_port(f'[::]:{config["port"]}')
  print(f'Escuchando en el puerto {config["port"]}')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    serve()
