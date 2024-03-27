import os
import shutil

def chaine_cond(chaine):  #vérifie l'existance du nombre d'arguments aprés la commande (ex: mv arg1 arg2)
    chaine_prime = chaine.split(' ')
    list_bool = []
    for i in chaine_prime:
        if i != '':
            list_bool.append(True)
        else:
            list_bool.append(False)
    return list_bool

def id_path(chaine):  #identification du type de chemin (absolu, relatif)
    id = 0
    list_chaine = []
    dirfile_cible = ''
    path_parent = ''
    if chaine.startswith('C:\\'):
        id = 1
    elif chaine.startswith('.\\') or ('\\') in chaine:
        id = 2
    elif not chaine.startswith('.\\') and not chaine.startswith('C:\\'):
        id = 3
    if id == 1 or id == 2:
        list_chaine = chaine.split('\\')
        dirfile_cible = list_chaine[-1]
        for i in range(len(list_chaine)):
            if list_chaine[i] != list_chaine[-1]:
                path_parent = path_parent + list_chaine[i] + '\\'
    elif id == 3:
        dirfile_cible = chaine
    return path_parent, dirfile_cible, id  #retourne respectivement le chemin parent, le dossier/fichier cible et le type de chemin

def pwd():
    print(os.getcwd())  #affiche le chemin de l'espace de travail

def cd(chaine):  #déplace l'espace de travail vers le chemin spécifié
    chaine = chaine.replace('cd', '').strip(' ')
    if os.path.isdir(chaine):
        try:
            os.chdir(chaine)
            print(os.getcwd())
        except FileNotFoundError:
            print('No such file or directory')
    else:
        print('No such file or directory')

def quite():  #quitte le programme
    os._exit(1)

def cd_racine():  #déplace l'espace de travail vers le chemin parent
    os.chdir(os.path.dirname(os.getcwd()))
    print(os.getcwd())

def ls():  #liste de dossiers et de fichiers dans le répertoire actuelle
    list_name = []
    list_name = os.listdir(os.getcwd())
    [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
    [print(x) for x in list_name if os.path.isfile(list_name[list_name.index(x)])]

def ls_l():  ##liste de dossiers et de fichiers dans le répertoire actuelle avec la taille en octets
    list_name = []
    list_name = os.listdir(os.getcwd())
    [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
    for i in range(len(list_name)):
        if os.path.isfile(list_name[i]):
            print(list_name[i] + ' ' + str(os.path.getsize(list_name[i])))

def ls_lh():  ##liste de dossiers et de fichiers dans le répertoire actuelle avec la taille en Byte, KB, MB, GB
    list_name = []
    list_name = os.listdir(os.getcwd())
    [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
    for i in range(len(list_name)):
        if os.path.isfile(list_name[i]):
            if int(os.path.getsize(list_name[i])) < 1000:
                print(list_name[i] + ' ' + str(round(os.path.getsize(list_name[i]))) + 'B')
            elif int(os.path.getsize(list_name[i])) >= 1000 and len(str(os.path.getsize(list_name[i]))) < 1000000:
                print(list_name[i] + ' ' + str(round(os.path.getsize(list_name[i]) / 1000)) + 'KB')
            elif int(os.path.getsize(list_name[i])) >= 1000000 and len(str(os.path.getsize(list_name[i]))) < 1000000000:
                print(list_name[i] + ' ' + str(round(os.path.getsize(list_name[i]) / 1000000)) + 'MB')
            elif int(os.path.getsize(list_name[i])) >= 1000000000 and len(str(os.path.getsize(list_name[i]))) < 1000000000000:
                print(list_name[i] + ' ' + str(round(os.path.getsize(list_name[i]) / 1000000000)) + 'GB')
  
def mkdir(chaine):  #crée un nouveau répertoire
    chaine = chaine.replace('mkdir', '').strip(' ')
    list_chaine = ''
    x = ''
    if chaine != '':
        list_chaine = os.path.split(chaine)
        result = id_path(chaine)
        path_parent = os.path.normpath(result[0])
        if result[2] == 3:
            x = result[1]
        if os.path.exists(result[0]):
            os.chdir(result[0])
            if list_chaine[-1] not in os.listdir(os.getcwd()):
                os.mkdir(result[1])
            else:
                print('The directory already exists')
        elif x != '':
            if list_chaine[-1] not in os.listdir(os.getcwd()):
                os.mkdir(result[1])
            else:
                print('The directory already exists')
    else:
        print('Specify the name of the directory to be made')

def rm(chaine):  #supprime un fichier ou un répertoire spécifié
    chaine = chaine.replace('rm', '').strip(' ')
    result = ''
    if chaine == '':
        print('Specify the file or directory')
    else:
        result = id_path(chaine)
        if result[-1] == 1:
            if os.path.isdir(chaine):
                try:
                    shutil.rmtree(chaine)
                except OSError:
                    print('No such file or directory')
            elif os.path.isfile(chaine):
                try:
                    os.remove(chaine)
                except FileNotFoundError:
                    print('No such file or directory')
        elif result[-1] == 2:
            os.chdir(result[0])
            if os.path.isdir(os.getcwd() + '\\' + result[1]):
                try:
                    shutil.rmtree(result[1])
                except OSError:
                    print('No such file or directory')
            elif os.path.isfile(os.getcwd() + '\\' + result[1]):
                try:
                    os.remove(result[1])
                except FileNotFoundError:
                    print('No such file or directory')
        elif result[-1] == 3:
            if os.path.isdir(os.getcwd() + '\\' + result[1]):
                try:
                    shutil.rmtree(result[1])
                except OSError:
                    print('No such file or directory')
            elif os.path.isfile(os.getcwd() + '\\' + result[1]):
                try:
                    os.remove(result[1])
                except FileNotFoundError:
                    print('No such file or directory')
            else:
                print('No such file or directory')

def mv(chaine):  #renomme n'importe quel fichier ou répertoire
    chaine = chaine.replace('mv', '').strip(' ')
    chaine_arg1_arg2 = chaine_cond(chaine)
    token_error = False
    chaine = chaine.split(' ')
    
    if chaine_arg1_arg2[0] != False:
        try:
            chaine_arg1_arg2[1]  #le positionnement de l'index indique le nombre d'argument à vérifier
        except IndexError:
            token_error = True
            print('Specify the current name of the file or directory and the new name')
    else:
        token_error = True
        print('Specify the current name of the file or directory and the new name')
    if token_error != True:
        if os.path.isdir(chaine[0]) or os.path.isfile(chaine[0]):
            if chaine[1] not in os.listdir(os.getcwd()):
                os.rename(chaine[0], chaine[1])
            else:
                print('The file or directory already exists')
        else:
            print('No such file or directory')

