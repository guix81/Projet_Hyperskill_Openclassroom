import os
import shutil

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
    chaine = chaine.replace('cd ', '')
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
    [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)]) and not '__pycache__']
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
    chaine = chaine.replace('mkdir ', '')
    chaine_bis = ''
    chaine_prime = ''
    if chaine != '':
        for i in reversed(range(len(chaine))):
            if '\\' != chaine[i]:
                chaine_bis = chaine_bis + chaine[i]
            else:
                break
        for i in reversed(range(len(chaine_bis))):
            chaine_prime = chaine_prime + chaine_bis[i]
        chaine = chaine.rstrip(chaine_prime)
        os.chdir(chaine)
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        if not os.path.exists(chaine + chaine_prime): 
            os.mkdir(chaine + chaine_prime)
        else:
            print('The directory already exists')
    else:
        print('Specify the name of the directory to be made')

def rm(chaine):  #supprime un fichier ou un répertoire spécifié
    chaine = chaine.replace('rm ', '')
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
    chaine = chaine.replace('mv ', '')
    chaine_prime = chaine.split(' ')
    new_chaine = ''
    new_chaine_bis = ''
    x = 0
    if chaine_prime != '':
        for i in range(len(chaine_prime)):
            if os.path.exists(new_chaine) == False:
                new_chaine = new_chaine + chaine_prime[i] + ' '
            else:
                x = i
                break
        for i in range(x, len(chaine_prime)):
            if os.path.exists(new_chaine_bis) == False:
                new_chaine_bis = new_chaine_bis + chaine_prime[i] + ' '
        new_chaine = new_chaine.strip(' ')
        new_chaine_bis = new_chaine_bis.strip(' ')
        if new_chaine_bis != '':
            result_1 = id_path(new_chaine)
            try:
                os.chdir(result_1[0])
            except FileNotFoundError:
                print('No such file or directory')
            result_2 = id_path(new_chaine_bis)
            if result_1[1] in os.listdir(os.getcwd()):
                if result_1[1] != result_2[1]:
                    os.rename(result_1[1], result_2[1])
                else:
                    print('The file or directory already exists')
            else:
                print('Specify the current name of the file or directory and the new name')
        else:
            print('Specify the current name of the file or directory and the new name')
    else:
            print('Specify the current name of the file or directory and the new name')




