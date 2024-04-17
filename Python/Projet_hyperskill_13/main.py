import sys

list_cmd = ['exit']

while True:
    choix = input()
    if choix.lower() == 'exit':
        print('Bye!')
        sys.exit(1)
    elif choix == '':
        print('No input.')
    else:
        print('Error: unknown command!')
    