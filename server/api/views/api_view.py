from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

peers_info = {}

@csrf_exempt
@api_view(['POST'])
def login(request):
  username = request.data.get('username')
  password = request.data.get('password')
  url = request.data.get('url')

  for peer, info in peers_info.items():
    if info['url'] == url:
      return Response({"message": "URL already registered."}, status=400)
    if peer == username:
      return Response({"message": "Username already registered."}, status=400)
  
  if not (username and url and password): 
    return Response({"message": "Username, Password and URL are required."}, status=400)
  
  peers_info[username] = {
    'url': url,
    'files': []
  }

  for peer in peers_info:
    print(peer, peers_info[peer])
  
  return Response({"message": "OK", "access_token": "123", "refresh_token" : "456"})

@csrf_exempt
@api_view(['POST'])
def logout(request):
  username = request.data.get('username')
  if username in peers_info:
    del peers_info[username]

    for peer in peers_info:
      print(peer, peers_info[peer])

    return Response({"message": "Logged out successfully."})
  else:
    return Response({"message": "Username not found."}, status=404)

@csrf_exempt
@api_view(['POST'])
def sendIndex(request):
  username = request.data.get('username')
  files = request.data.get('files')
  
  if username not in peers_info:
    return Response({"message": "Peer not logged in."}, status=404)
  
  if not files:
    return Response({"message": "No files provided."}, status=400)
  
  # Actualizar la lista de archivos para el peer
  peers_info[username]['files'] = files
  
  return Response({"message": "Index updated successfully."})

@csrf_exempt
@api_view(['GET'])
def query(request):
  filename = request.query_params.get('filename')
  
  if not filename:
    return Response({"message": "Filename is required."}, status=400)
  
  peers_with_file = [info['url'] for username, info in peers_info.items() if 'files' in info and filename in info['files']]
  
  if not peers_with_file:
    return Response({"message": "File not found."}, status=404)
  
  return Response({"urls": peers_with_file})




