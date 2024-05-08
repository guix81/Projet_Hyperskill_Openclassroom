import package as pac


class User(pac.Shell):
    def __init__(self, name, password, status='offline', id_=''):
        self.name = name
        self.password = password
        self.log = False
        self.status = status
        self.id = id_
        if id_ == '':
            self.id = 'u' + pac.add_id(pac.Shell.list_user)
        pac.maj_data(self.__repr__(), pac.Shell.list_user, 'data_user.csv', pac.Shell.head_user)
        pac.Shell.list_obj_user.append(self)

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
        title = input("Veuillez saisir le titre du thread: ")
        content = input("Veuillez saisir le texte: ")
        post = pac.Post(content, self.name)
        thread = pac.Thread(title, self.name)
        thread.obj_posts.append(post)
        thread.list_id_posts.append(post.id)
        pac.Shell.list_threads.append(thread.__repr__())
        pac.modif_database(thread, pac.Shell.list_obj_thread, pac.Shell.list_threads, 'data_threads.csv', pac.Shell.head_thread, key='liste_id_post', value=post.id)

    def add_post(self, obj_thread):
        post = pac.Post("yoyo !", self.name)
        index = pac.Shell.list_obj_thread.index(obj_thread)
        pac.Shell.list_obj_thread[index].obj_posts.append(post)
        pac.Shell.list_obj_thread[index].list_id_posts.append(post.id)  # todo: en construction

    def modif_post(self):
        pass

    def del_post(self):
        pass

    def __str__(self):
        return f"Pseudo: {self.name}, Satus: {self.status}"
    
    def __repr__(self):
        return {'name': self.name, 'pass': self.password, 'status': self.status, 'id': self.id, 'autority': 'User'}
    
class Moderateur(User):
    AUTORITY = "Modo"

    def __str__(self):
        return super().__str__() + ', ' + f"Autority: {Moderateur.AUTORITY}"
    
    def __repr__(self):
        x = super().__repr__()
        x['autority'] = Moderateur.AUTORITY
        return x
    
class Admin(User):
    AUTORITY = "Admin"

    def __str__(self):
        return super().__str__() + ', ' + f"Autority: {Admin.AUTORITY}"
    
    def __repr__(self):
        x = super().__repr__()
        x['autority'] = Admin.AUTORITY
        return x


