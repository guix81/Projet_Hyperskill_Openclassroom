import random

class Operation:  # centre d'opération
    list_sign = ['+', '-', '*']
    
    def __init__(self, chaine_op):
        self.chaine_op = chaine_op
        self.arg1 = ''
        self.arg2 = ''
        self.sign = ''
        self.result = ''
    
    def decoupage(self):  # découpe la chaine pour interprétation
        for i in self.chaine_op:
            if i in Operation.list_sign:
                if self.chaine_op[self.chaine_op.index(i) - 1] == ' ' and self.chaine_op[self.chaine_op.index(i) + 1] == ' ':
                    self.chaine_op = self.chaine_op.split(' ')
    
    def verif_arg(self):  # définit les arguments et le signe
        x = 0
        for i in range(len(self.chaine_op)):
            if self.chaine_op[i].isdigit():
                self.arg1 = self.arg1 + self.chaine_op[i]
            else:
                x = i
                break
        for i in range(x, len(self.chaine_op)):
                if self.chaine_op[i] in Operation.list_sign:
                    self.sign = self.sign + self.chaine_op[i]
        for i in range(x, len(self.chaine_op)):
                if self.chaine_op[i].isdigit():
                    self.arg2 = self.arg2 + self.chaine_op[i] 

    def calc(self): # calcul l'opération
        if self.sign == '+':
            self.result = str(int(self.arg1) + int(self.arg2))
        elif self.sign == '-':
            self.result = str(int(self.arg1) - int(self.arg2))
        elif self.sign == '*':
            self.result = str(int(self.arg1) * int(self.arg2))
        return int(self.result)
    
    def carre(self):  # clacule le carré du nombre
        return int(self.chaine_op) ** 2
    
class BotOp1(Operation):
    def __init__(self):
        self.arg_1 = ''
        self.arg_2 = ''
        self.sign_ = ''
        self.string_op = ''

    def genere(self):  # génère une opération aléatoire
        self.arg_1 = str(random.randint(2, 9))
        self.arg_2 = str(random.randint(2, 9))
        self.sign_ = random.choice(Operation.list_sign)
        self.string_op = self.arg_1 + ' ' + self.sign_ + ' ' + self.arg_2
        return self.string_op

    def printed(self):  # affiche l'opération
        print(self.string_op)

class BotOp2(Operation):
    def __init__(self):
        self.arg_1 = ''

    def genere(self):  # génère un nombre aléatoire (calcule du carré par l'utilisateur)
        self.arg_1 = str(random.randint(11, 29))
        return self.arg_1

    def printed(self):  # affiche l'opération
        print(self.arg_1)

def bot_test_1():
    bot = BotOp1()
    op = Operation(bot.genere())
    
    bot.printed()
    op.decoupage()
    op.verif_arg()
    solution = op.calc()
    return solution

def test_operation_simple():  # génère un test (opérations simples avec les nombres 2-9)
    compt = 0
    n_sol = 0
    while compt < 5:
        sol = bot_test_1()
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

def bot_test_2():
    bot = BotOp2()
    op = Operation(bot.genere())
    
    bot.printed()
    solution = op.carre()
    return solution

def test_carre():  # génère un test (carrés intégraux 11-29)
    compt = 0
    n_sol = 0
    while compt < 5:
        sol = bot_test_2()
        while True:
            reponse = input()
            if reponse.isdigit():
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