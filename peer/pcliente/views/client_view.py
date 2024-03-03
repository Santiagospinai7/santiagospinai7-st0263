from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from ..config import config

@api_view(['GET'])
def login(request):
  data = config['peer_info']
  response = requests.post(f"{config['server_url']}login/", json=data)
  return JsonResponse(response.json())

@api_view(['GET'])
def logout(request):
  data = {"username": config['peer_info']['username']}
  response = requests.post(f"{config['server_url']}logout/", json=data)
  return JsonResponse(response.json())

@api_view(['GET'])
def send_index(request):
  data = {
    "username": config['peer_info']['username'],
    "files": ["file1.txt", "file2.txt"]  # Ejemplo de lista de archivos
  }
  response = requests.post(f"{config['server_url']}sendIndex/", json=data)
  return JsonResponse(response.json())

@api_view(['GET'])
def query(request):
  # Obtener el nombre del archivo desde los parámetros de la solicitud GET
  filename = request.GET.get('filename')
  if not filename:
    return JsonResponse({"error": "Filename is required."}, status=400)
  
  # Realizar la solicitud al servidor central
  response = requests.get(f"{config['server_url']}query/?filename={filename}")
  
  # Devolver la respuesta del servidor central al peer solicitante
  if response.status_code == 200:
    return JsonResponse(response.json())
  else:
    return JsonResponse({"error": "File not found or error in query."}, status=response.status_code)

