import string

import package as pac



class User(pac.Shell):
    def __init__(self, name, password, status='offline'):
        self.name = name
        self.password = password
        self.log = False
        self.status = status
        pac.maj_data_user(self.__repr__())

    def login(self):
        while True:
            log_name = input("Veuillez rentrez votre pseudo: ")
            if log_name == self.name:
                log_password = input("Veuillez rentrez votre mot de pass: ")
                if log_password == self.password:
                    self.log = True
                    break
                else:
                    print("Mot de pass invalide")
            else:
                print("Pseudo invalide")
        if self.log:
            self.status = 'online'
        else:
            self.status = 'offline'

    def add_thread(self):
        title = string.capwords(input("Veuillez saisir un titre pour le thread: "))
        thread = pac.Thread(title, self.name)  # à exporter dans une base de donnée de type json
        return thread

    def add_post(self, thread):
        pass

    def modif_post(self):
        pass

    def del_post(self):
        pass

    def __str__(self):
        return f"Pseudo: {self.name}, Satus: {self.status}"
    
    def __repr__(self):
        return [self.name, self.password, self.status]
    
class Moderateur(User):
    AUTORITY = "Modo"

    def __str__(self):
        return super().__str__() + ', ' + f"Autority: {Moderateur.AUTORITY}"
    
    def __repr__(self):
        return pac.tuple_to_list(super().__repr__(), Admin.AUTORITY)
    
class Admin(User):
    AUTORITY = "Admin"

    def __str__(self):
        return super().__str__() + ', ' + f"Autority: {Admin.AUTORITY}"
    
    def __repr__(self):
        return pac.tuple_to_list(super().__repr__(), Admin.AUTORITY)


