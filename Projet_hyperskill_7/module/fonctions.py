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

def rm(chaine):  #supprime un fichier ou un répertoire spécifié os.remove() chutil.rmtree() [en construction]
    chaine = chaine.replace('rm ', '')
    token = None
    if chaine == '':
        print('Specify the file or directory')
    else:
        os.chdir(chaine)
        path_parent = os.path.dirname(os.getcwd())
        current_path = os.getcwd()
        os.chdir(path_parent)
        if os.path.isdir(current_path):
            try:
                os.rmdir(current_path)
                token = True
            except OSError:
                token = False
                print('erreur3')
            if token == False:
                while True:
                    path_parent = os.path.dirname(os.getcwd())
                    current_path = os.getcwd()
                    os.chdir(current_path)
                    list_filedir = os.listdir(current_path)
                    for y in list_filedir:
                        if os.path.isdir(path_parent + '\\' + y):
                            os.chdir(path_parent + '\\' + y)
                            break
                        else:
                            os.remove(path_parent + '\\' + y)
                    listbool = []
                    [listbool.append(os.path.isdir(path_parent + '\\' + x)) for x in range(len(list_filedir))]
                    if False in listbool:
                        print('listbool')
                        break
                    else:
                        print('nolistbool')
                        break
            else:
                print('erreur1')
        elif os.path.isfile(current_path):
            try:
                os.remove(current_path)
            except FileNotFoundError:
                print('No such file or directory')       
        else:
            print('erreur2')
        

def mv():  #renomme n'importe quel fichier ou répertoire
    pass

def mkdir():  #crée un nouveau répertoire
    pass

