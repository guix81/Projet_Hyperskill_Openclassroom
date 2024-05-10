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
        thread.list_id_posts = thread.list_id_posts + ' ' + post.id
        pac.Shell.list_threads.append(thread.__repr__())
        pac.modif_database(thread, 
                           pac.Shell.list_obj_thread,  
                           'data_threads.csv', 
                           pac.Shell.head_thread, 
                           key='liste_id_post', 
                           value=thread.list_id_posts, 
                           mode='modif_val')
        pac.Shell.list_obj_thread.append(thread)

    def add_post(self, obj_thread):
        content = input("Veuillez saisir le texte: ")
        post = pac.Post(content, self.name)
        obj_thread.obj_posts.append(post)
        obj_thread.list_id_posts = obj_thread.list_id_posts + ' ' + post.id
        pac.modif_database(obj_thread, 
                           pac.Shell.list_obj_thread,  
                           'data_threads.csv', 
                           pac.Shell.head_thread, 
                           key='liste_id_post', 
                           value=obj_thread.list_id_posts, 
                           mode='modif_val')

    def __str__(self):
        return f"Pseudo: {self.name}, Satus: {self.status}"
    
    def __repr__(self):
        return {'name': self.name, 'pass': self.password, 'status': self.status, 'id': self.id, 'autority': 'User'}
    
class Moderateur(User):
    AUTORITY = "Modo"

    def modif_post(self, obj_post):
        content = input("Veuillez saisir le nouveau texte: ")
        if self.name == obj_post.username:
            pac.modif_database(obj_post, 
                            pac.Shell.list_obj_post,  
                            'data_posts.csv', 
                            pac.Shell.head_post, 
                            key='content_post', 
                            value=content, 
                            mode='modif_val')
            
    def del_post(self, obj_post):
        for thread in pac.Shell.list_obj_thread:
            if obj_post.id in thread.list_id_posts:
                chaine = thread.list_id_posts.split(' ')
                list_id = ''
                for id in chaine:
                    if id == obj_post.id:
                        continue
                    id = id.strip(' ')
                    list_id = ' ' + list_id + ' ' + id
                thread.list_id_posts = list_id.strip(' ')
                pac.modif_database(thread, 
                                    pac.Shell.list_obj_thread, 
                                    'data_threads.csv', 
                                    pac.Shell.head_thread, 
                                    key='liste_id_post', 
                                    value=list_id.strip(' '), 
                                    mode='modif_val')
                    
                pac.modif_database(obj_post, 
                                    pac.Shell.list_obj_post,  
                                    'data_posts.csv', 
                                    pac.Shell.head_post, 
                                    mode='del')
            else:
                pac.modif_database(obj_post, 
                                    pac.Shell.list_obj_post,  
                                    'data_posts.csv', 
                                    pac.Shell.head_post, 
                                    mode='del')
                                       
    def __str__(self):
        return super().__str__() + ', ' + f"Autority: {Moderateur.AUTORITY}"
    
    def __repr__(self):
        x = super().__repr__()
        x['autority'] = Moderateur.AUTORITY
        return x
    
class Admin(Moderateur):
    AUTORITY = "Admin"

    def del_thread(self, obj_thread):
        chaine = obj_thread.list_id_posts.split(' ')
        list_id = []
        for id in chaine:
            list_id.append(id)
        for post in pac.Shell.list_obj_post:
            if post.id in list_id:
                print(None)
                pac.modif_database(post, 
                                pac.Shell.list_obj_post,  
                                'data_posts.csv', 
                                pac.Shell.head_post, 
                                mode='del')

        pac.modif_database(obj_thread, 
                            pac.Shell.list_obj_thread,  
                            'data_threads.csv', 
                            pac.Shell.head_thread, 
                            mode='del')

    def __str__(self):
        return super().__str__() + ', ' + f"Autority: {Admin.AUTORITY}"
    
    def __repr__(self):
        x = super().__repr__()
        x['autority'] = Admin.AUTORITY
        return x


