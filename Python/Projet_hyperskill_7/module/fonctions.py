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
    if chaine.startswith('C:\\') or chaine.startswith('\\Home\\'):
        id = 1
    elif chaine.startswith('.\\') or ('\\') in chaine:
        id = 2
    else:
        id = 3
    if id == 1 or id == 2:
        list_chaine = chaine.split('\\')
        dirfile_cible = list_chaine[-1]
        for i in range(len(list_chaine)):
            if list_chaine[i] != list_chaine[-1]:
                path_parent = path_parent + list_chaine[i] + '\\'
            else:
                path_parent = path_parent.strip('\\')
    elif id == 3:
        dirfile_cible = chaine
    return path_parent, dirfile_cible, id  #retourne respectivement le chemin parent, le dossier/fichier cible et le type de chemin

def pwd():  ##affiche le chemin de l'espace de travail
    print(os.getcwd())

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
    chaine_args = chaine_cond(chaine)
    token_error = False
    list_extension = ['.txt']
    error_extention = False
    bool_isdir_file = []
    chaine = chaine.split(' ')
    
    if chaine_args[0] != False:
        try:
            chaine_args[0]  #le positionnement de l'index indique le nombre minimum d'argument à vérifier
        except IndexError:
            token_error = True
            print('Specify the current name of the file or directory and the new location and/or name')
    else:
        token_error = True
        print('Specify the file or directory')
    if token_error != True:
        result_1 = id_path(chaine[0])
        if result_1[2] == 1 or result_1[2] == 2:
            if os.path.isfile(chaine[0]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(chaine[0]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(chaine[0]):
                bool_isdir_file.append('noExist')
        elif result_1[2] == 3:
            if os.path.isfile(result_1[1]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(result_1[1]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(result_1[1]):
                bool_isdir_file.append('noExist')

        if result_1[1] not in list_extension:
            error_extention = True

        if bool_isdir_file[0] == 'isDir':
            if result_1[2] == 1 or result_1[2] == 2:
                shutil.rmtree(chaine[0])
            else:
                shutil.rmtree(result_1[1])
        elif bool_isdir_file[0] == 'isFile':
            if result_1[2] == 1 or result_1[2] == 2:
                os.remove(chaine[0])
            else:
                os.remove(result_1[1])
        elif bool_isdir_file[0] == 'noExist' and result_1[1] in list_extension:
            for i in os.listdir('.'):
                if i.endswith(result_1[1]):
                    os.remove(i)
        elif error_extention == True:
            print(f'File extension {result_1[1]} not found in this directory')
        else:
            print('No such file or directory')

def mv(chaine):  #renomme n'importe quel fichier ou répertoire
    chaine = chaine.replace('mv', '').strip(' ')
    chaine_args = chaine_cond(chaine)
    token_error = False
    list_extension = ['.txt']
    error_extention = False
    bool_isdir_file = []
    chaine = chaine.split(' ')
    
    if chaine_args[0] != False:
        try:
            chaine_args[1]  #le positionnement de l'index indique le nombre d'argument à vérifier
        except IndexError:
            token_error = True
            print('Specify the current name of the file or directory and the new location and/or name')
    else:
        token_error = True
        print('Specify the current name of the file or directory and the new location and/or name')
    if token_error != True:
        result_1 = id_path(chaine[0])
        result_2 = id_path(chaine[1])
        if result_1[2] == 1 or result_1[2] == 2:
            if os.path.isfile(chaine[0]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(chaine[0]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(chaine[0]):
                bool_isdir_file.append('noExist')
        elif result_1[2] == 3:
            if os.path.isfile(result_1[1]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(result_1[1]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(result_1[1]):
                bool_isdir_file.append('noExist')
        
        if result_2[2] == 1 or result_2[2] == 2:
            if os.path.isfile(chaine[1]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(chaine[1]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(chaine[1]):
                bool_isdir_file.append('noExist')
        elif result_2[2] == 3:
            if os.path.isfile(result_2[1]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(result_2[1]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(result_2[1]):
                bool_isdir_file.append('noExist')

        if result_1[1] not in list_extension:
            error_extention = True

        if chaine_args[0] == False or bool_isdir_file[1] == 'noExist':
            print('No such file or directory')
        
        if bool_isdir_file[0] == 'isFile' and bool_isdir_file[1] == 'isDir':
            if result_1[1] not in os.listdir(chaine[1]):
                if result_1[2] == 1 or result_1[2] == 2:
                    shutil.move(chaine[0], chaine[1])
                else:
                    shutil.move(result_1[1], chaine[1])
            else:
                print('The file or directory already exists')
        elif bool_isdir_file[0] == 'isFile' and not bool_isdir_file[1] == 'noExist' and result_2[2] == 3:
            if result_2[1] not in os.listdir('.'):
                if result_1[2] == 1 or result_1[2] == 2:
                    os.rename(chaine[0], result_2[1])
                else:
                    os.rename(result_1[1], result_2[1])
            else:
                print('The file or directory already exists')
        elif bool_isdir_file[0] == 'isFile' and bool_isdir_file[1] == 'noExist':
            if result_2[1] not in os.listdir('.'):
                if result_1[2] == 1 or result_1[2] == 2:
                    shutil.move(chaine[0], chaine[1])
                else:
                    shutil.move(result_1[1], chaine[1])
            else:
                print('The file or directory already exists')
        elif bool_isdir_file[0] == 'noExist' and error_extention != True and bool_isdir_file[1] == 'isDir':
            for i in os.listdir('.'):
                if result_2[2] == 1 or result_2[2] == 2:
                    if i.endswith(chaine[1]):
                        if i not in os.listdir(chaine[1]):
                            shutil.move(i, chaine[1])
                        else:
                            while True:
                                r = input(f'{i} already exists in this directory. Replace? (y/n)')
                                if r == 'y':
                                    os.remove(chaine[1] + '\\' + i)
                                    shutil.move(i, chaine[1])
                                    break
                                elif r == 'n':
                                    break
                else:
                    if i.endswith(result_1[1]):
                        if i not in os.listdir(result_2[1]):
                            shutil.move(i, result_2[1])
                        else:
                            while True:
                                r = input(f'{i} already exists in this directory. Replace? (y/n)')
                                if r == 'y':
                                    path_abs = os.path.abspath(result_2[1] + '/' + i)
                                    os.remove(path_abs)
                                    shutil.move(i, result_2[1])
                                    break
                                elif r == 'n':
                                    break
        elif error_extention == True:
            print(f'File extension {result_1[1]} not found in this directory')

def cp(chaine):  #copie un fichier et enregistre cette copie dans un nouveau répertoire 
    chaine = chaine.replace('cp', '').strip(' ')
    chaine_args = chaine_cond(chaine)
    nb_args = 1  # index 0 + 1 = 2 args
    token_error = False
    bool_isdir_file = []
    list_extension = ['.txt']
    error_extention = False
    chaine = chaine.split(' ')
    
    if chaine_args[0] != False:
        try:
            chaine_args[nb_args]  #le positionnement de l'index indique le nombre d'argument à vérifier
            try:
                chaine_args[nb_args + 1]  #n'accepte pas de troisième argument
                token_error = True
                print('Specify the current name of the file or directory and the new location and/or name')
            except IndexError:
                token_error = False
        except IndexError:
            token_error = True
            print('Specify the current name of the file or directory and the new location and/or name')
    else:
        token_error = True
        print('Specify the file')

    if token_error != True:
        result_1 = id_path(chaine[0])
        result_2 = id_path(chaine[1])
        if result_1[2] == 1 or result_1[2] == 2:
            if os.path.isfile(chaine[0]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(chaine[0]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(chaine[0]):
                bool_isdir_file.append('noExist')
        elif result_1[2] == 3:
            if os.path.isfile(result_1[1]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(result_1[1]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(result_1[1]):
                bool_isdir_file.append('noExist')
        
        if result_2[2] == 1 or result_2[2] == 2:
            if os.path.isfile(chaine[1]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(chaine[1]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(chaine[1]):
                bool_isdir_file.append('noExist')
        elif result_2[2] == 3:
            if os.path.isfile(result_2[1]):
                bool_isdir_file.append('isFile')
            elif os.path.isdir(result_2[1]):
                bool_isdir_file.append('isDir')
            elif not os.path.exists(result_2[1]):
                bool_isdir_file.append('noExist')
            elif result_2[1] == '..':
                bool_isdir_file.append('..')  #cd racine

        if result_1[1] not in list_extension:
            error_extention = True

        if chaine_args[0] == False or bool_isdir_file[1] == 'noExist':
            print('No such file or directory')

        elif bool_isdir_file[0] == 'isFile' and bool_isdir_file[1] == 'isDir':
            if result_1[1] not in os.listdir(chaine[1]):
                if result_1[2] == 1 or result_1[2] == 2:
                    shutil.copy(chaine[0], chaine[1])
                else:
                    shutil.copy(result_1[1], chaine[1])
            else:
                print(f'{result_1[1]} already exists in this directory')
        elif bool_isdir_file[0] == 'isFile' and bool_isdir_file[1] == '..':
            if result_1[1] not in os.listdir(os.path.dirname(chaine[1])):
                if result_1[2] == 1 or result_1[2] == 2:
                    shutil.copy(chaine[0], result_2[0])
                else:
                    shutil.copy(result_1[1], result_2[0])
            else:
                print(f'{result_1[1]} already exists in this directory')
        elif bool_isdir_file[0] == 'noExist' and error_extention != True and bool_isdir_file[1] == 'isDir':
            for i in os.listdir('.'):
                if result_2[2] == 1 or result_2[2] == 2:
                    if i.endswith(chaine[0]):
                        if i not in os.listdir(chaine[1]):
                            shutil.copy(i, chaine[1])
                        else:
                            while True:
                                r = input(f'{i} already exists in this directory. Replace? (y/n)')
                                if r == 'y':
                                    os.remove(chaine[1] + '\\' + i)
                                    shutil.copy(i, chaine[1])
                                    break
                                elif r == 'n':
                                    break
                else:
                    if i.endswith(result_1[1]):
                        if i not in os.listdir(result_2[1]):
                            shutil.copy(i, result_2[1])
                        else:
                            while True:
                                r = input(f'{i} already exists in this directory. Replace? (y/n)')
                                if r == 'y':
                                    t = os.path.abspath(result_2[1] + '/' + i)
                                    os.remove(t)
                                    shutil.copy(i, result_2[1])
                                    break
                                elif r == 'n':
                                    break
        elif bool_isdir_file[0] == 'noExist' and error_extention != True and result_2[1] == '..':
            x = os.path.dirname(os.getcwd())
            for i in os.listdir('.'):
                if i.endswith(result_1[1]):
                    if i not in os.listdir(x):
                        shutil.copy(i, x)
                    else:
                        while True:
                            r = input(f'{i} already exists in this directory. Replace? (y/n)')
                            if r == 'y':
                                os.remove(x + '\\' + i)
                                shutil.copy(i, x)
                                break
                            elif r == 'n':
                                break
        elif error_extention == True:
            print(f'File extension {result_1[1]} not found in this directory')
                

