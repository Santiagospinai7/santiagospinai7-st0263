from django.core.management.base import BaseCommand
from pcliente.views import logout as logout_view

class Command(BaseCommand):
  help = 'Realiza un logout al servidor central.'

  def handle(self, *args, **kwargs):
    response = logout_view(None)
    print(response.content)
