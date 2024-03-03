from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['POST'])
def login(request):
    # Aquí iría la lógica para manejar el login, por ahora solo devolvemos un OK
    return Response({"message": "OK"})


