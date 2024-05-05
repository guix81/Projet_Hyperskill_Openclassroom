import os
import csv
import random
import package as pac


#------------------------------------------------------Fonction init_main--------------------------------------------------------------------

def init_main():
    init_data_user()
    init_obj_user()
    init_data_posts()
    init_obj_post()
    init_data_threads()
    #init_obj_thread()

#----------------------------------------------------Fonctions réutilisable------------------------------------------------------------------

def add_id(shell_list):
    while True:
        id_ = str(random.randint(1, 10000))
        if id_ in shell_list:
            pass
        else:
            return id_

def _repr_to_list(_repr_):
    x = []
    for i in _repr_:
        x.append(i)
    return x

def extract_data_csv(path, file_csv, shell_head, dest_shell_list):
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
    os.chdir(current_path)

def maj_data(obj__repr__, dest_shell_list, file_csv, shell_head):  # Ajoute le __repr__ de l'objet dans le fichier data.csv
    current_path = os.getcwd()
    dest_path = os.getcwd() + '\\Python\\Cours_openclassroom\\forum\\data'
    if current_path != dest_path:
        os.chdir(dest_path)

    if obj__repr__ not in dest_shell_list:
        with open(file_csv, "a", newline='', encoding='utf-8') as file:
            data_a = csv.DictWriter(file, delimiter=',', fieldnames=shell_head)
            data_a.writerow(obj__repr__)
    os.chdir(current_path)

#-------------------------------------------------Fonctions lié à la class User--------------------------------------------------------------

def init_data_user():  # initialise la récupération des données du fichier data.csv
    extract_data_csv('\\Python\\Cours_openclassroom\\forum\\data', 'data_user.csv', pac.Shell.head_user, pac.Shell.list_user)

def init_obj_user():  # recréé une liste d'objet user dans le shell
    for data_user in pac.Shell.list_user:
        if data_user != pac.Shell.head_user:
            obj = get_user_csv(data_user)
            pac.Shell.list_obj_user.append(obj)

def get_user_csv(data_user):  # récupère le __repr__ de l'objet non-instancié du fichier data_user.csv et recréé l'instance de cet objet.
    index = pac.Shell.list_user.index(data_user)
    if pac.Shell.list_user[index]["autority"] == 'Admin':
        return pac.Admin(pac.Shell.list_user[index]['name'], 
                         pac.Shell.list_user[index]['pass'], 
                         status=pac.Shell.list_user[index]['status'], 
                         id_=pac.Shell.list_user[index]['id'])
    elif pac.Shell.list_user[index]["autority"] == 'Modo':
        return pac.Moderateur(pac.Shell.list_user[index]['name'], 
                              pac.Shell.list_user[index]['pass'], 
                              status=pac.Shell.list_user[index]['status'], 
                              id_=pac.Shell.list_user[index]['id'])
    elif pac.Shell.list_user[index]["autority"] == 'User':
        return pac.User(pac.Shell.list_user[index]['name'], 
                        pac.Shell.list_user[index]['pass'], 
                        status=pac.Shell.list_user[index]['status'], 
                        id_=pac.Shell.list_user[index]['id'])

#-------------------------------------------------Fonctions lié à la class Thread------------------------------------------------------------

def init_data_threads():
    extract_data_csv('\\Python\\Cours_openclassroom\\forum\\data', 'data_threads.csv', pac.Shell.head_thread, pac.Shell.list_threads)

def init_obj_thread():
    for data_thread in pac.Shell.list_threads:
        if data_thread != pac.Shell.head_thread:
            obj = get_thread_csv(data_thread)
            pac.Shell.list_obj_thread.append(obj)

def get_thread_csv(data_thread):  # todo: lié les objet Post à l'objet Thread par id
    index = pac.Shell.list_threads.index(data_thread)
    return pac.Thread(pac.Shell.list_threads[index][0], 
                      pac.Shell.list_threads[index][1], 
                      date_in=pac.Shell.list_threads[index][2], 
                      id_=pac.Shell.list_threads[index][3], 
                      list_id_post=pac.Shell.list_threads[index][4])

#--------------------------------------------------Fonctions lié à la class Post-------------------------------------------------------------

def init_data_posts():
    extract_data_csv('\\Python\\Cours_openclassroom\\forum\\data', 'data_posts.csv', pac.Shell.head_post, pac.Shell.list_posts)

def init_obj_post():
    for data_post in pac.Shell.list_posts:
        if data_post != pac.Shell.head_post:
            obj = get_post_csv(data_post)
            pac.Shell.list_obj_post.append(obj)

def get_post_csv(data_post):
    index = pac.Shell.list_posts.index(data_post)
    return pac.Post(pac.Shell.list_posts[index]["content_post"], 
                    pac.Shell.list_posts[index]["username_post"], 
                    date_in=pac.Shell.list_posts[index]["date_post"], 
                    id_=pac.Shell.list_posts[index]['id'])