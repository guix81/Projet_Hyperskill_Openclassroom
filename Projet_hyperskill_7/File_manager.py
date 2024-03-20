import os


print('Input the command')
list_command = ('pwd', 'cd..', 'cd ', 'quit', )
while True:
    chaine = input()
    while True:
        if chaine.startswith(list_command) == False:
            print('Invalid command')
            print(os.getcwd())
            break
        else:
            break
    if chaine == 'pwd':
        print(os.getcwd())
    elif chaine.startswith('cd ') == True:
        try:
            chaine = chaine.lstrip('cd ')
            os.chdir(chaine)
            print(os.getcwd())
        except(OSError):
            print('Invalid command')
            print(os.getcwd())
            break
    elif chaine == 'quite':
        os._exit(1)
    elif chaine == 'cd..':
        os.chdir(os.path.dirname(os.getcwd()))
        print(os.getcwd())
