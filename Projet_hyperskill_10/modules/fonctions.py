import sys

class Equation:
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n):" 
    msg_5 = "Do you want to continue calculations? (y / n):"
    list_result = [0]

    def __init__(self, chaine):  # equation chaine
        self.chaine = chaine
        self.x = 0
        self.y = 0
        self.oper = ''
        self.result = 0.0
        self.list_bool = []  # validation des méthodes

    def init(self, obj):
        self.list_bool.clear()
        obj.tri_chaine()
        obj.verif_xy()
        obj.verif_oper()
        obj.calc()
        obj.store_result()
        #obj.display()

    def tri_chaine(self):  # decoupe la chaine x oper y
        self.chaine = self.chaine.split(' ')

    def verif_xy(self):
        if self.chaine[0] == 'M':
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
        self.list_bool.append(True)
        
    def verif_oper(self):
        if False not in self.list_bool:
            list_sign = ['-', '+', '*', '/']

            if self.chaine[1] in list_sign:
                self.oper = self.chaine[1]
                self.list_bool.append(True)
                return # valide x oper y
            else:
                print(self.msg_2)
                self.list_bool.append(False)
                return
        
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
                return
    
    def store_result(self):
        if False not in self.list_bool:
            while True:
                print(self.msg_4)
                rep = input()
                if rep == 'y':
                    self.list_result.append(self.list_result[-1] + self.result)
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

    def display(self):
        print(self.chaine)
        print(self.x)
        print(self.y)
        print(self.oper)
        print(self.result)
        print(self.list_result)
        print(self.list_bool)  


        
                

                
