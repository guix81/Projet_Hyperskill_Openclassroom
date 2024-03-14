import random

random.seed()

n_pencil_max = int(input('How many pencils would you like to use:\n'))
token_john = False
token_jack = False


while True:
    first_player = input('Who will be the first (John, Jack):\n')
    if first_player == 'John' or first_player == 'Jack':
        break

if first_player == 'John':
    token_john = True
    #n_barre = random.randint(1, n_pencil_max)
    print(n_pencil_max * '|')
elif first_player == 'Jack':
    token_jack = True
    #n_barre = random.randint(1, n_pencil_max)
    print(n_pencil_max * '|')

while n_pencil_max > 0:
    if token_john == True:
        print("John's turn:")
        n_barre = int(input())
        n_pencil_max = n_pencil_max - n_barre
        print(n_pencil_max * '|')
        token_john = False
        token_jack = True
    elif token_jack == True:
        print("Jack's turn:")
        n_barre = int(input())
        n_pencil_max = n_pencil_max - n_barre
        print(n_pencil_max * '|')
        token_john = True
        token_jack = False
