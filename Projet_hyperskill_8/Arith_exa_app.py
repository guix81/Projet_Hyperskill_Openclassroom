from modules.fonctions import test_operation_simple, test_carre


while True:
    rep = input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n''')
    if rep == '1':
        test_operation_simple()
        break
    elif rep == '2':
        test_carre()
        break
    elif rep == 'quite':
        break
    else:
        print('Incorrect format.')
