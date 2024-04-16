import modules.fonction as mf


ri = mf.Ring()
ri.read_file('rating.txt')
ri.analyse_file()
name = input('Enter your name: ')

if name in ri.base_score.keys():
    player = mf.Player(name, ri.base_score[name])
else:
    player = mf.Player(name, '0')
    ri.write_init('rating.txt', player)
    ri.reanalyse(player)
print(f'Hello, {name}')

while True:
    choice = input().strip(',')
    if choice != '':
        ri.list_option = choice.split(',')
        print(ri.list_option)
        print(mf.Ring.ref_option)
        for i in ri.list_option:
            if i not in mf.Ring.ref_option:
                ri.list_option.clear()
    break
print("Okay, let's start")
if ri.list_option == []:
    mf.jeu_defaut(ri, player)
else:
    mf.jeu_custom(ri, player)

