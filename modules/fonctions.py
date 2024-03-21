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

def seek_chaine(chaine_1, chaine_2):
    if chaine_2 in chaine_1:
        return True
    else:
        return False

