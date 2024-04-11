import sys

class Equation:
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n):" 
    msg_5 = "Do you want to continue calculations? (y / n):"
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg_10 = "Are you sure? It is only one digit! (y / n)"
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
    list_msg = [msg_10, msg_11, msg_12]
    list_result = [0]

    def __init__(self, chaine):  # equation chaine
        self.chaine = chaine
        self.x = 0
        self.y = 0
        self.oper = ''
        self.result = 0.0
        self.msg = ''
        self.msg_index = 0
        self.list_bool = []  # validation des méthodes

    def init(self, obj):
        self.list_bool.clear()
        obj.tri_chaine()
        obj.verif_xy()
        obj.verif_oper()
        obj.check()
        obj.calc()
        obj.store_result()
        #obj.display()

    def tri_chaine(self):  # decoupe la chaine x oper y
        self.chaine = self.chaine.split(' ')

    def verif_xy(self):
        if self.chaine[0] == 'M' and self.chaine[2] == 'M':
            self.x = self.list_result[-1]
            self.y = self.list_result[-1]
        elif self.chaine[0] == 'M':
            self.x = self.list_result[-1]
        elif self.chaine[2] == 'M':
            self.y = self.list_result[-1]
        
        if self.chaine[0] != 'M':
            try:
                self.x = int(self.chaine[0])
            except ValueError:
                try:
                    self.x = float(self.chaine[0])
                except ValueError:
                    print(self.msg_1)
                    self.list_bool.append(False)
                    return
                
        if self.chaine[2] != 'M':
            try:
                self.y = int(self.chaine[2])
            except ValueError:
                try:
                    self.y = float(self.chaine[2])
                except ValueError:
                    print(self.msg_1)
                    self.list_bool.append(False)
                    return
        self.list_bool.append(True)  # valide x, y
        
    def verif_oper(self):
        if False not in self.list_bool:
            list_sign = ['-', '+', '*', '/']
            if self.chaine[1] in list_sign:
                self.oper = self.chaine[1]
                self.list_bool.append(True)  # valide oper
                return
            else:
                print(self.msg_2)
                self.list_bool.append(False)
                return
            
    def is_one_digit(self, xy):
        if xy > -10 and xy < 10 and float(xy).is_integer():
            return True
        else:
            return False

    def check(self):
        if self.is_one_digit(self.x) and self.is_one_digit(self.y):
            self.msg = self.msg + self.msg_6
        if (self.x == 1 or self.y == 1) and self.oper == '*':
            self.msg = self.msg + self.msg_7
        if (self.x == 0 or self.y == 0) and (self.oper == '*' or self.oper == '+' or self.oper == '-'):
            self.msg = self.msg + self.msg_8
        if self.msg != '':
            self.msg = self.msg_9 + self.msg
            print(self.msg)
        
    def calc(self):
        if False not in self.list_bool:
            if self.oper == '+':
                self.result = float(self.x + self.y)
                print(self.result)
                self.list_bool.append(True)
            elif self.oper == '-':
                self.result = float(self.x - self.y)
                print(self.result)
                self.list_bool.append(True)
            elif self.oper == '*':
                self.result = float(self.x * self.y)
                print(self.result)
                self.list_bool.append(True)
            elif self.oper == '/' and self.y != 0:
                self.result = float(self.x / self.y)
                print(self.result)
                self.list_bool.append(True)
            else:
                print(self.msg_3)
                self.list_bool.append(False)
    
    def store_result(self):  # mémorise le résultat
        if False not in self.list_bool:
            rep_1 = ''
            while True:
                if rep_1 == 'n':
                    break
                elif not self.msg_index < 2:
                    break
                print(self.msg_4)
                rep = input()
                if rep == 'y':
                    if self.is_one_digit(self.result):
                        self.msg_index = 0
                        while True:
                            print(self.list_msg[self.msg_index])
                            rep_1 = input()
                            if rep_1 == 'y':
                                if self.msg_index < 2:
                                    self.msg_index += 1
                                else:
                                    self.list_result.append(self.result)
                                    break
                            elif rep_1 == 'n':
                                break
                    else:
                        self.list_result.append(self.result)
                        break
                elif rep == 'n':
                    break
            while True:
                print(self.msg_5)
                rep = input()
                if rep == 'y':
                    break
                elif rep == 'n':
                    sys.exit(1)

    def display(self):  # debug
        print(self.chaine)
        print(self.x)
        print(self.y)
        print(self.oper)
        print(self.result)
        print(self.list_result)
        print(self.list_bool)  


        
                

                
