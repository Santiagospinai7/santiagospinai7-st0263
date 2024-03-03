from django.core.management.base import BaseCommand
from pcliente.views import query as query_view

class Command(BaseCommand):
  help = 'Realiza una consulta al servidor central.'

  def handle(self, *args, **kwargs):
    response = query_view(None, filename=kwargs['filename'])
    print(response.content)
