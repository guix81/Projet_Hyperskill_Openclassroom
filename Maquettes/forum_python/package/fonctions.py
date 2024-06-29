import os
import csv
import random

import package as pac


#------------------------------------------------------Fonction init_main--------------------------------------------------------------------

def init_main():
    """Fonction qui initialise l'extraction des datas des fichiers csv puis recréér les objets issue de celles-ci"""
    a = init_data_user()
    b = init_obj_user()
    c = init_username()
    d = init_data_posts()
    e = init_obj_post()
    f = init_data_threads()
    i = init_obj_thread()
    r = a + b + c + d + e + f + i
    if r == 7:
        return True
    else:
        return False

#----------------------------------------------------Fonctions réutilisable------------------------------------------------------------------

def modif_database(shell_obj, shell_obj_list, file_csv, shell_head, key=None, value=None, mode=None):
    """Modifie la data dans un fichier csv spécifié."""
    line = []
    current_path = os.getcwd()
    dest_path = os.getcwd() + pac.Shell.path_data
    if current_path != dest_path:
        os.chdir(dest_path)
    with open(file_csv, "r+", newline='', encoding='utf-8') as file:
        data_m = csv.DictReader(file, delimiter=',')
        for datam in data_m:
            if shell_obj.__repr__()['id'] == datam['id']:
                if mode == 'modif_val':
                    if (key != None) and (value != None):
                        datam[key] = value
                elif mode == 'del':
                    continue
            line.append(datam)
    with open(file_csv, "w", newline='', encoding='utf-8') as file:
        data_w = csv.DictWriter(file, delimiter=',', fieldnames=shell_head)
        data_w.writeheader()
        for line_ in line:
            data_w.writerow(line_)
    try:
        index = shell_obj_list.index(shell_obj)
        shell_obj_list.pop(index)
    except TypeError:
        pass
    os.chdir(current_path)
    init_obj_post()
    return True

def add_id(shell_list):
    """Permet d'assossier un élément (user, post, thread) à un id."""
    while True:
        id_ = str(random.randint(1, 10000))
        if id_ in shell_list:
            pass
        else:
            return id_

def extract_data_csv(path, file_csv, shell_head, dest_shell_list):
    """Permet d'extraire la data des fichiers csv."""
    token = False
    current_path = os.getcwd()
    dest_path = os.getcwd() + path
    
    if current_path != dest_path:
        os.chdir(dest_path)
    
    if file_csv not in os.listdir('.'):  # Si le fichier n'existe pas, il sera créé avec une en-tête.
        with open(file_csv, "w", newline='', encoding='utf-8') as file:
            data_w = csv.DictWriter(file, delimiter=',', fieldnames=shell_head)
            data_w.writeheader()
    
    with open(file_csv, "r", newline='', encoding='utf-8') as file:  # Lecture du fichier data pour récupérer les données dans le shell.
        data_r = csv.DictReader(file, delimiter=',')
        for i in data_r:
            dest_shell_list.append(i)
        token = True
    os.chdir(current_path)
    return token

def maj_data(shell_obj_repr_, dest_shell_list, file_csv, shell_head):
    """Ajoute le __repr__ de l'objet dans le fichier data.csv."""
    current_path = os.getcwd()
    dest_path = os.getcwd() + pac.Shell.path_data
    if current_path != dest_path:
        os.chdir(dest_path)

    if shell_obj_repr_ not in dest_shell_list:
        with open(file_csv, "a", newline='', encoding='utf-8') as file:
            data_a = csv.DictWriter(file, delimiter=',', fieldnames=shell_head)
            data_a.writerow(shell_obj_repr_)
    os.chdir(current_path)

def verif_data(file_csv, shell_obj):
    """Vérifie l'existance d'une data dans le fichier csv."""
    current_path = os.getcwd()
    dest_path = os.getcwd() + pac.Shell.path_data
    if current_path != dest_path:
        os.chdir(dest_path)
    with open(file_csv, "r", newline='', encoding='utf-8') as file:
        data_m = csv.DictReader(file, delimiter=',')
        for datam in data_m:
            if shell_obj.__repr__()['id'] == datam['id']:
                os.chdir(current_path)
                return True
        os.chdir(current_path)
        return False

#-------------------------------------------------Fonctions lié à la class User--------------------------------------------------------------

def init_data_user():
    """initialise la récupération des données du fichier data_user.csv."""
    return extract_data_csv(pac.Shell.path_data, 'data_user.csv', pac.Shell.head_user, pac.Shell.list_user)

def init_obj_user():
    """recréé une liste d'objet user dans le shell"""
    for data_user in pac.Shell.list_user:
        if data_user != pac.Shell.head_user:
            obj = get_user_csv(data_user)
            if (isinstance(obj, pac.Admin) or isinstance(obj, pac.Moderateur) or isinstance(obj, pac.User)) == False:
                return False
    return True

def get_user_csv(data_user):
    """récupère le __repr__ de l'objet non-instancié du fichier data_user.csv et recréé l'instance de cet objet."""
    index = pac.Shell.list_user.index(data_user)
    if pac.Shell.list_user[index]["autority"] == 'Admin':
        return pac.Admin(pac.Shell.list_user[index]['name'], 
                         pac.Shell.list_user[index]['mdp'], 
                         status=pac.Shell.list_user[index]['status'], 
                         id_=pac.Shell.list_user[index]['id'])
    elif pac.Shell.list_user[index]["autority"] == 'Modo':
        return pac.Moderateur(pac.Shell.list_user[index]['name'], 
                              pac.Shell.list_user[index]['mdp'], 
                              status=pac.Shell.list_user[index]['status'], 
                              id_=pac.Shell.list_user[index]['id'])
    elif pac.Shell.list_user[index]["autority"] == 'User':
        return pac.User(pac.Shell.list_user[index]['name'], 
                        pac.Shell.list_user[index]['mdp'], 
                        status=pac.Shell.list_user[index]['status'], 
                        id_=pac.Shell.list_user[index]['id'])
    
def creat_compte():
    """Créer un compte pour l'utilisateur"""
    token = False
    while True:
        pseudo = input("Veuillez choisir votre pseudo: ")
        for obj_name in pac.Shell.list_obj_user:
            if pseudo == obj_name.name:
                print('Ce pseudo est déja pris!')
                break
            else:
                mdp = input("Veuillez choisir un mot de pass: ")
                user = pac.User(pseudo, mdp)
                token = True
                break
        if token:
            break

def init_username():
    """utilisé pour éviter les doublons de pseudo dans la base de donnée."""
    for obj_user in pac.Shell.list_obj_user:
        pac.Shell.list_username.append(obj_user.name)
    return True

#-------------------------------------------------Fonctions lié à la class Thread------------------------------------------------------------

def init_data_threads():
    """initialise la récupération des données du fichier data_threads.csv."""
    return extract_data_csv(pac.Shell.path_data, 'data_threads.csv', pac.Shell.head_thread, pac.Shell.list_threads)

def init_obj_thread():
    """recréé une liste d'objet thread dans le shell"""
    for data_thread in pac.Shell.list_threads:
        if data_thread != pac.Shell.head_thread:
            obj = get_thread_csv(data_thread)
            if isinstance(obj, pac.Thread) == False:
                return False
    return True

def get_thread_csv(data_thread):
    """récupère le __repr__ de l'objet non-instancié du fichier data_threads.csv et recréé l'instance de cet objet."""
    index = pac.Shell.list_threads.index(data_thread)
    return pac.Thread(pac.Shell.list_threads[index]["title_thread"], 
                      pac.Shell.list_threads[index]["username_thread"], 
                      date_in=pac.Shell.list_threads[index]["date_trhead"], 
                      id_=pac.Shell.list_threads[index]["id"], 
                      list_id_posts=pac.Shell.list_threads[index]["liste_id_post"])

def print_all_thread():
    """print et renvoie le nombre de thread"""
    x = 1
    list_ = []
    for thread in pac.Shell.list_obj_thread:
        print(str(x) + ": " + thread.title)
        list_.append(x)
        x += 1
    return list_


#--------------------------------------------------Fonctions lié à la class Post-------------------------------------------------------------

def init_data_posts():
    """initialise la récupération des données du fichier data_posts.csv."""
    return extract_data_csv(pac.Shell.path_data, 'data_posts.csv', pac.Shell.head_post, pac.Shell.list_posts)

def init_obj_post():
    """recréé une liste d'objet post dans le shell"""
    for data_post in pac.Shell.list_posts:
        if data_post != pac.Shell.head_post:
            obj = get_post_csv(data_post)
            if isinstance(obj, pac.Post) == False:
                return False
    return True

def get_post_csv(data_post):
    """récupère le __repr__ de l'objet non-instancié du fichier data_posts.csv et recréé l'instance de cet objet."""
    index = pac.Shell.list_posts.index(data_post)
    return pac.Post(pac.Shell.list_posts[index]["content_post"], 
                    pac.Shell.list_posts[index]["username_post"], 
                    date_in=pac.Shell.list_posts[index]["date_post"], 
                    id_=pac.Shell.list_posts[index]['id'])

def print_all_posts(thread):
    """print et renvoie le nombre de post"""
    x = 1
    list_ = []
    for posts in thread.obj_posts:
        print(str(x) + ": " + str(posts.__repr__()))
        list_.append(x)
        x += 1
    return list_ 

#------------------------------------------------------------Front-end-----------------------------------------------------------------------

def front():
    """Initialise le pupitre pour l'utilisateur (dans le terminal)"""
    instance = pac.MenuLogin()
    instance.display_action()
