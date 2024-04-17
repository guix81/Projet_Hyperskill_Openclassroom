import random

list_invite = []
dict_invite = {}
nb_invite = int(input('Enter the number of friends joining (including you):'))

if nb_invite > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(nb_invite):
        list_invite.append(input())
    dict_invite = dict.fromkeys(list_invite, 0)
    facture_total = int(input('Enter the total bill value:'))
    facture_partage = round(facture_total / nb_invite, 2)

    for key in dict_invite.keys():
        dict_invite[key] = facture_partage

    choix = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    while choix != 'Yes' or choix != 'No':
        if choix == 'Yes':
            random.seed()
            rand_invite = random.choice(list_invite)
            print(f'{rand_invite} is the lucky one!')
            facture_partage = round(facture_total / (nb_invite - 1), 2)
            for key in dict_invite.keys():
                if key != rand_invite:
                    dict_invite[key] = facture_partage
                else:
                    dict_invite[key] = 0
            break
        elif choix == 'No':
            print('No one is going to be lucky')
            break

    print(dict_invite)
else:
    print('No one is joining for the party')

