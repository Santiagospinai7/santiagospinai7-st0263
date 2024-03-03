import argparse
from django.core.management import call_command

def main():
  parser = argparse.ArgumentParser(description='CLI para interactuar con el servidor central.')
  parser.add_argument('--action', choices=['login', 'logout', 'send_index', 'query'], help='Acción a realizar')
  parser.add_argument('--filename', help='Nombre del archivo para la acción query')

  args = parser.parse_args()

  if args.action == 'login':
    call_command('login')
  elif args.action == 'logout':
    call_command('logout')
  elif args.action == 'send_index':
    call_command('send_index')
  elif args.action == 'query' and args.filename:
    call_command('query', filename=args.filename)
  else:
    print("Acción no reconocida o falta de argumentos necesarios.")

if __name__ == '__main__':
  main()
