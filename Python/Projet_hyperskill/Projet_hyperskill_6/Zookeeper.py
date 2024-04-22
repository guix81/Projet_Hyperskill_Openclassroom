import string

from modules.fonctions import valide_input

animals = ['camel', 'lion', 'deer', 'goose', 'bat', 'rabbit']
token_exit = False

while True:
    while True:
        chaine = input('Please enter the number of the habitat you would like to view:')
        error = valide_input(chaine, string.ascii_letters, '')
        if error[1] != True:
            chaine = int(chaine)
            break
        elif error[2] == True:
            token_exit = True
            break
        else:
            print('Entrer une valeur correct')
    if token_exit == False:
        if (chaine <= len(animals)) and (chaine >= 0):
            print(animals[chaine])
    if chaine == 'exit':
        break
print("See you later!")