import os
import csv
import random
import sys

import package as pac


#------------------------------------------------------Fonction init_main--------------------------------------------------------------------

def init_main():
    init_data_user()
    init_obj_user()
    init_username()
    init_data_posts()
    init_obj_post()
    init_data_threads()
    init_obj_thread()

#----------------------------------------------------Fonctions réutilisable------------------------------------------------------------------

def modif_database(shell_obj, shell_obj_list, file_csv, shell_head, key=None, value=None, mode=None):
    line = []
    current_path = os.getcwd()
    dest_path = os.getcwd() + '\\Python\\Cours_openclassroom\\forum\\data'
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

def add_id(shell_list):
    while True:
        id_ = str(random.randint(1, 10000))
        if id_ in shell_list:
            pass
        else:
            return id_

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

def maj_data(shell_obj_repr_, dest_shell_list, file_csv, shell_head):  # Ajoute le __repr__ de l'objet dans le fichier data.csv
    current_path = os.getcwd()
    dest_path = os.getcwd() + '\\Python\\Cours_openclassroom\\forum\\data'
    if current_path != dest_path:
        os.chdir(dest_path)

    if shell_obj_repr_ not in dest_shell_list:
        with open(file_csv, "a", newline='', encoding='utf-8') as file:
            data_a = csv.DictWriter(file, delimiter=',', fieldnames=shell_head)
            data_a.writerow(shell_obj_repr_)
    os.chdir(current_path)

#-------------------------------------------------Fonctions lié à la class User--------------------------------------------------------------

def init_data_user():  # initialise la récupération des données du fichier data.csv
    extract_data_csv('\\Python\\Cours_openclassroom\\forum\\data', 'data_user.csv', pac.Shell.head_user, pac.Shell.list_user)

def init_obj_user():  # recréé une liste d'objet user dans le shell
    for data_user in pac.Shell.list_user:
        if data_user != pac.Shell.head_user:
            get_user_csv(data_user)

def get_user_csv(data_user):  # récupère le __repr__ de l'objet non-instancié du fichier data_user.csv et recréé l'instance de cet objet.
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
    for obj_user in pac.Shell.list_obj_user:
        pac.Shell.list_username.append(obj_user.name)

#-------------------------------------------------Fonctions lié à la class Thread------------------------------------------------------------

def init_data_threads():
    extract_data_csv('\\Python\\Cours_openclassroom\\forum\\data', 'data_threads.csv', pac.Shell.head_thread, pac.Shell.list_threads)

def init_obj_thread():
    for data_thread in pac.Shell.list_threads:
        if data_thread != pac.Shell.head_thread:
            get_thread_csv(data_thread)

def get_thread_csv(data_thread):
    index = pac.Shell.list_threads.index(data_thread)
    return pac.Thread(pac.Shell.list_threads[index]["title_thread"], 
                      pac.Shell.list_threads[index]["username_thread"], 
                      date_in=pac.Shell.list_threads[index]["date_trhead"], 
                      id_=pac.Shell.list_threads[index]["id"], 
                      list_id_posts=pac.Shell.list_threads[index]["liste_id_post"])

def print_all_thread():
    x = 1
    list_ = []
    for thread in pac.Shell.list_obj_thread:
        print(str(x) + ": " + thread.title)
        list_.append(x)
        x += 1
    return list_


#--------------------------------------------------Fonctions lié à la class Post-------------------------------------------------------------

def init_data_posts():
    extract_data_csv('\\Python\\Cours_openclassroom\\forum\\data', 'data_posts.csv', pac.Shell.head_post, pac.Shell.list_posts)

def init_obj_post():
    for data_post in pac.Shell.list_posts:
        if data_post != pac.Shell.head_post:
            get_post_csv(data_post)

def get_post_csv(data_post):
    index = pac.Shell.list_posts.index(data_post)
    return pac.Post(pac.Shell.list_posts[index]["content_post"], 
                    pac.Shell.list_posts[index]["username_post"], 
                    date_in=pac.Shell.list_posts[index]["date_post"], 
                    id_=pac.Shell.list_posts[index]['id'])

def print_all_posts(thread):
    x = 1
    list_ = []
    for posts in thread.obj_posts:
        print(str(x) + ": " + str(posts.__repr__()))
        list_.append(x)
        x += 1
    return list_ 

#------------------------------------------------------------Front-end-----------------------------------------------------------------------

def front():
    instance = pac.MenuLogin()
    instance.display_action()