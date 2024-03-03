from django.core.management.base import BaseCommand
from pcliente.views import login as login_view

class Command(BaseCommand):
  help = 'Realiza un login al servidor central.'

  def handle(self, *args, **kwargs):
    response = login_view(None)
    print(response.content)
