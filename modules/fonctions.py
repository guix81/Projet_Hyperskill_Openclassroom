def valide_input(chaine_input, chaine_auto, chaine_no_auto):  #Attention, le type de variable d'entrée doit rester une chaine.
    token_alpha = None
    token_num = None
    token_auto = None
    token_no_auto = None
    try:  #True si chaine_input = numeric [token_num]
        chaine_input = int(chaine_input)
        token_num = True
    except(ValueError):
        token_num = False
    if type(chaine_input) == type('a'):  ##True si chaine_input = alphabétique or alphanumérique [token_chaine]
        token_alpha = True
    else:
        token_alpha = False
    chaine_input = str(chaine_input)
    chaine_auto = set(chaine_auto)  #True si chaine_input est 'seulement' dans la liste des caractère autoriser(chaine_auto) [token_auto]
    for str_in in chaine_input:
        if str_in not in chaine_auto:
            token_auto = False
            break
        else:
            token_auto = True
    chaine_no_auto = set(chaine_no_auto) #True si chaine_input est 'seulement' dans la liste des caractère non-autoriser(chaine_no_auto) [token_no_auto]
    for str_in in chaine_input:
            if str_in in chaine_no_auto:
                token_no_auto = True
                break
            else:
                token_no_auto = False
    return token_num, token_alpha, token_auto, token_no_auto  #revoie une liste bool [token_num, token_chaine, token_auto, token_no_auto]

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
                os.remove(current_path)
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