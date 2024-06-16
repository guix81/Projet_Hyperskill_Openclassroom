import sys

import package as pac

class MenuLogin(pac.Shell):
    user_instance = None
    def __init__(self):
        self.user = None
        self.login_user = False

    def action_1(self):  # Se connecter à votre compte 
        while True:
            choice_s = input("Veuillez saisir votre pseudo: ")
            for obj_name in pac.Shell.list_obj_user:
                if choice_s in pac.Shell.list_username:
                    r = obj_name.login()
                    if r == False:
                        break
                    if obj_name.log:
                        self.user = obj_name
                        MenuLogin.user_instance = obj_name
                        self.login_user = True
                        print("vous êtes connecté!")
                        break
                else:
                    print("Le pseudo que vous avez saisi n'existe pas!")
                    break
            if self.login_user:
                break
        if MenuLogin.user_instance.__repr__()['autority'] == 'User':
            menu_user = MenuUser()
            menu_user.display_action()
        elif MenuLogin.user_instance.__repr__()['autority'] == 'Modo':
            menu_modo = MenuModo()
            menu_modo.display_action()
        elif MenuLogin.user_instance.__repr__()['autority'] == 'Admin':
            menu_admin = MenuAdmin()
            menu_admin.display_action()
    
    def action_2(self):  # Créer un compte sur le forum
        pac.creat_compte()

    def action_3(self):  # Quitter le programme
        sys.exit(1)

    def display_action(self):
        while True:
            print("\n1: Se connecter à votre compte") 
            print("2: Créer un compte sur le forum")
            print("3: Quitter le programme\n")
            choice = input("Faite votre choix: ")
            if choice == '1':
                self.action_1()
            elif choice == '2':
                self.action_2()
            elif choice == '3':
                self.action_3()

class MenuUser(MenuLogin):
    def action_4(self):  # Créer un thread
        MenuLogin.user_instance.add_thread()

    def action_5(self):  # Créer un post
        while True:
            list_index_thread = pac.print_all_thread()
            index = int(input("Veuillez choisir un thread: "))
            if index in list_index_thread:
                index = index - 1
                MenuLogin.user_instance.add_post(pac.Shell.list_obj_thread[int(index)])
                break

    def action_6(self):  # Déconnexion
        self.login_user = False
        MenuLogin.user_instance.deconnect()
        MenuLogin.user_instance = None

    def display_action(self):
        while True:
            print("\n1: Créer un thread") 
            print("2: Créer un post")
            print("3: Déconnexion\n")
            choice = input("Faite votre choix: ")
            if choice == '1':
                self.action_4()
            elif choice == '2':
                self.action_5()
            elif choice == '3':
                self.action_6()
                break

class MenuModo(MenuUser):
    def action_7(self):  # Modifier un post
        while True:
            list_index_thread = pac.print_all_thread()
            index = int(input("Veuillez choisir un thread: "))
            if index in list_index_thread:
                index = index - 1
                break
        thread = pac.Shell.list_obj_thread[index]
        thread.display()
        while True:
            list_index_post = pac.print_all_posts(thread)
            index_post = int(input("Veuillez choisir un post à modifier: "))
            if index_post in list_index_post:
                index_post = index - 1
                MenuLogin.user_instance.modif_post(thread.obj_posts[index_post])
                break

    def action_8(self):  # Supprimer un post
        while True:
            list_index_thread = pac.print_all_thread()
            index = int(input("Veuillez choisir un thread: "))
            if index in list_index_thread:
                index -= 1
                break
        thread = pac.Shell.list_obj_thread[index]
        thread.display()
        while True:
            list_index_post = pac.print_all_posts(thread)
            index_post = int(input("Veuillez choisir un post à supprimer: "))
            if index_post in list_index_post:
                index_post -= 1
                MenuLogin.user_instance.del_post(thread.obj_posts[index_post])
                break

    def display_action(self):
        while True:
            print("\n1: Créer un thread") 
            print("2: Créer un post")
            print("3: Modifier un post")
            print("4: Supprimer un post")
            print("5: Déconnexion\n")
            choice = input("Faite votre choix: ")
            if choice == '1':
                self.action_4()
            elif choice == '2':
                self.action_5()
            elif choice == '3':
                self.action_7()
            elif choice == '4':
                self.action_8()
            elif choice == '5':
                self.action_6()
                break

class MenuAdmin(MenuUser):
    def action_9(self):  # Supprimer un thread
        while True:
            list_index_thread = pac.print_all_thread()
            index = int(input("Veuillez choisir un thread: "))
            if index in list_index_thread:
                index -= 1
                MenuLogin.user_instance.del_thread(pac.Shell.list_obj_thread[index])
                break

    def display_action(self):
        while True:
            print("\n1: Créer un thread") 
            print("2: Créer un post")
            print("3: Modifier un post")
            print("4: Supprimer un thread")
            print("5: Supprimer un post")
            print("6: Déconnexion\n")
            choice = input("Faite votre choix: ")
            if choice == '1':
                self.action_4()
            elif choice == '2':
                self.action_5()
            elif choice == '3':
                self.action_7()
            elif choice == '4':
                self.action_9()
            elif choice == '5':
                self.action_8()
            elif choice == '6':
                self.action_6()
                break