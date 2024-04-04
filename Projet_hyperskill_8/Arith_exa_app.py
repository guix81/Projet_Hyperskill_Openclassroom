from modules.fonctions import bot_test

compt = 0
n_sol = 0
while compt < 5:
    sol = bot_test()
    while True:
        reponse = input()
        if reponse.isdigit() or (reponse[1:].isdigit() and ('-' in reponse[0])):
            if int(reponse) == sol:
                print('Right!')
                compt += 1
                n_sol += 1
                break
            else:
                print('Wrong!')
                compt += 1
                break
        else:
            print('Incorrect format')

print(f'Your mark is {n_sol}/5.')

