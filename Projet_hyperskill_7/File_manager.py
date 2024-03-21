import os
import time
import shutil

from module.fonctions import pwd, cd, cd_racine, quite, ls, ls_l, ls_lh

print('Input the command')
list_command = ('pwd', 'cd..', 'cd ', 'quite', 'ls', 'ls -l', 'ls -lh')
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
        pwd()
    elif chaine.startswith('cd ') == True:
        try:
            cd(chaine)
        except(OSError):
            print(chaine)
            break
    elif chaine == 'quite':
        quite()
    elif chaine == 'cd..':
        cd_racine()
    elif chaine == 'ls':
        ls(list_name)
    elif chaine == 'ls -l':
        ls_l(list_name)
    elif chaine == 'ls -lh':
        ls_lh(list_name)

    
