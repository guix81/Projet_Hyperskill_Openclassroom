import os
import shutil

def pwd():
    print(os.getcwd())  #affiche le chemin de l'espace de travail

def cd(chaine):  #déplace l'espace de travail vers le chemin spécifié
    chaine = chaine.replace('cd ', '')
    os.chdir(chaine)
    print(os.getcwd())

def quite():  #quitte le programme
    os._exit(1)

def cd_racine():  #déplace l'espace de travail vers le chemin parent
    os.chdir(os.path.dirname(os.getcwd()))
    print(os.getcwd())

def ls(list_name):  #liste de dossiers et de fichiers dans le répertoire actuelle
    list_name.clear()
    list_name = os.listdir(os.getcwd())
    [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
    [print(x) for x in list_name if os.path.isfile(list_name[list_name.index(x)])]

def ls_l(list_name):  ##liste de dossiers et de fichiers dans le répertoire actuelle avec la taille en octets
    list_name.clear()
    list_name = os.listdir(os.getcwd())
    [print(x) for x in list_name if os.path.isdir(list_name[list_name.index(x)])]
    for i in range(len(list_name)):
        if os.path.isfile(list_name[i]):
            print(list_name[i] + ' ' + str(os.path.getsize(list_name[i])))

def ls_lh(list_name):  ##liste de dossiers et de fichiers dans le répertoire actuelle avec la taille en Byte, KB, MB, GB
    list_name.clear()
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

def rm():  #supprime un fichier ou un répertoire spécifié
    pass

def mv():  #renomme n'importe quel fichier ou répertoire
    pass

def mkdir():  #crée un nouveau répertoire
    pass

