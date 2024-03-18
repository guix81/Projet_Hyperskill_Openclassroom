import string

from modules.fonction import valide_input
from modules.fonction import bot_pencil

def first_player(name_1, name_2):  #définit le jeton premier joueur
    while True:
        first_player = input(f'Who will be the first ({name_1}, {name_2}):\n')
        if first_player == name_1 or first_player == name_2:
            break
        else:
            print(f'Choose between {name_1} and {name_2}')
    if first_player == name_1: 
        print(n_pencil_max * '|')
        return name_1
    elif first_player == name_2:
        print(n_pencil_max * '|')
        return name_2

print('How many pencils would you like to use:')
while True:
    n_pencil_max = input()
    x = valide_input(n_pencil_max, '', '-')
    if x[0] == True:
        if int(n_pencil_max) != 0:
            if (x[3] == True):
                print('The number of pencils should be numeric')
            else:
                break
        else:
            print('The number of pencils should be positive')
    else:
        print('The number of pencils should be numeric')
n_pencil_max = int(n_pencil_max)
PENCIL_MAX = n_pencil_max

first_name = first_player('John', 'Jack')
token_john = False
token_jack = False


if first_name == 'John':
    token_john = True
elif first_name == 'Jack':
    token_jack = True

while n_pencil_max >= 0:
    if token_john == True:
        print("John's turn:")
        while True:
            n_barre = input()
            y = valide_input(n_barre, '123', '-')
            if (y[2] != True) or (int(n_barre) > 3) or (y[1] == True):
                print("Possible values: '1', '2' or '3'")
            elif int(n_barre) > n_pencil_max:
                print('Too many pencils were taken')
            else:
                break
        n_barre = int(n_barre)     
        n_pencil_max = n_pencil_max - n_barre
        print(n_pencil_max * '|')
        token_john = False
        token_jack = True
        if n_pencil_max < 1:
            print('Jack won!')
            break
    elif token_jack == True:
        print("Jack's turn:")
        n_barre = bot_pencil(n_pencil_max, PENCIL_MAX)
        n_pencil_max = n_pencil_max - n_barre
        print(n_barre)
        print(n_pencil_max * '|')
        token_john = True
        token_jack = False
        if n_pencil_max < 1:
            print('John won!')
            break
