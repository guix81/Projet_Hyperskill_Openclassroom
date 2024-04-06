from modules.fonctions import test_operation_simple, test_carre, score


while True:
    rep = input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n''')
    if rep == '1':
        result = test_operation_simple()
        score(result[0], result[1])
        break
    elif rep == '2':
        result = test_carre()
        score(result[0], result[1])
        break
    elif rep == 'quite':
        break
    else:
        print('Incorrect format.')
