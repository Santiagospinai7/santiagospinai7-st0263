from django.core.management.base import BaseCommand
from pcliente.views import send_index as send_index_view

class Command(BaseCommand):
  help = 'Envía el index al servidor central.'

  def handle(self, *args, **kwargs):
    response = send_index_view(None)
    print(response.content)
