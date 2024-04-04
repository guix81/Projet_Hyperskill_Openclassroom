from modules.fonctions import bot_test

while True:
    x = bot_test()
    if int(input()) == x:
        print('Right!')
    else:
        print('Wrong!')


