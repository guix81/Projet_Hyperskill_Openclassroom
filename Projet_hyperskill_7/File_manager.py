import os
import string

print('Input the command')
list_command = ('pwd', 'cd..', 'cd ', 'quit', 'ls', 'ls -l', 'ls -lh')
list_name = []
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
            chaine = chaine.replace('cd ', '')
            os.chdir(chaine)
            print(os.getcwd())
        except(OSError):
            print(chaine)
            break
    elif chaine == 'quite':
        os._exit(1)
    elif chaine == 'cd..':
        os.chdir(os.path.dirname(os.getcwd()))
        print(os.getcwd())
    elif chaine == 'ls':
        list_name.clear()
        list_name = os.listdir(os.getcwd())
        [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
        [print(x) for x in list_name if os.path.isfile(list_name[list_name.index(x)])]
        print(os.getcwd())
    elif chaine == 'ls -l':
        list_name.clear()
        list_name = os.listdir(os.getcwd())
        [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
        for i in range(len(list_name)):
            if os.path.isfile(list_name[i]):
                print(list_name[i] + ' ' + str(os.path.getsize(list_name[i])))
        print(os.getcwd())
    elif chaine == 'ls -lh':
        list_name.clear()
        list_name = os.listdir(os.getcwd())
        [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
        for i in range(len(list_name)):
            if os.path.isfile(list_name[i]):
                if len(str(os.path.getsize(list_name[i]))) < 1000:
                    print(list_name[i] + ' ' + str(os.path.getsize(list_name[i])) + 'B')
                elif len(str(os.path.getsize(list_name[i]))) >= 1000 and len(str(os.path.getsize(list_name[i]))) < 1000000:
                    print(list_name[i] + ' ' + str(os.path.getsize(list_name[i]) / 1000) + 'KB')
                elif len(str(os.path.getsize(list_name[i]))) >= 1000000 and len(str(os.path.getsize(list_name[i]))) < 1000000000:
                    print(list_name[i] + ' ' + str(os.path.getsize(list_name[i]) / 1000000) + 'MB')
                elif len(str(os.path.getsize(list_name[i]))) >= 1000000000 and len(str(os.path.getsize(list_name[i]))) < 1000000000000:
                    print(list_name[i] + ' ' + str(os.path.getsize(list_name[i]) / 1000000000) + 'GB')

    
