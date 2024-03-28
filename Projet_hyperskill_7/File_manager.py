import os

from module.fonctions import pwd, cd, cd_racine, quite, ls, ls_l, ls_lh, rm, mv, mkdir, cp

print('Input the command')
list_command = ('pwd', 'cd..', 'cd', 'quite', 'ls', 'ls -l', 'ls -lh', 'rm', 'mv', 'mkdir', 'cp')
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
    elif chaine.startswith('cd'):
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
        ls()
    elif chaine == 'ls -l':
        ls_l()
    elif chaine == 'ls -lh':
        ls_lh()
    elif chaine.startswith('rm'):
        rm(chaine)
    elif chaine.startswith('mv'):
        mv(chaine)
    elif chaine.startswith('mkdir'):
        mkdir(chaine)
    elif chaine.startswith('cp'):
        cp(chaine)


    
