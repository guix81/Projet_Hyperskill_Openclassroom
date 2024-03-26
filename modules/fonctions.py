import os

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

def id_path(chaine):  #identification du type de chemin (absolu, relatif)
    id = 0
    list_chaine = []
    dirfile_cible = ''
    path_parent = ''
    if chaine.startswith('C:\\'):
        id = 1
    elif chaine.startswith('.\\'):
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



    


    


