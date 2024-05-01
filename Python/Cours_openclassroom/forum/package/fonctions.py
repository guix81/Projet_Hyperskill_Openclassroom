import os
import csv
import package as pac


#------------------------------------------------------Fonction init_main--------------------------------------------------------------------

def init_main():
    init_data_user()
    init_obj_user()

#----------------------------------------------------Fonctions réutilisable------------------------------------------------------------------
def _repr_to_list(_repr_):
    x = []
    for i in _repr_:
        x.append(i)
    return x

def extract_data_csv(path, file_csv, head, dest_list):
    current_path = os.getcwd()
    dest_path = os.getcwd() + path
    if current_path != dest_path:
        os.chdir(dest_path)

    if file_csv not in os.listdir('.'):  # Si le fichier n'existe pas, il sera créé avec une en-tête.
        with open(file_csv, "w", newline='', encoding='utf-8') as file:
            data_w = csv.writer(file, delimiter=',')
            data_w.writerow(head)
    
    with open(file_csv, "r", newline='', encoding='utf-8') as file:  # Lecture du fichier data pour récupérer les données dans le shell.
        data_r = csv.reader(file, delimiter=',')
        for i in data_r:
            dest_list.append(i)
    os.chdir(current_path)

#-------------------------------------------------Fonctions lié à la class User--------------------------------------------------------------

def maj_data_user(obj__repr__, dest_list, file_csv):  # Ajoute le __repr__ de l'objet User dans le fichier data_user.csv
    current_path = os.getcwd()
    dest_path = os.getcwd() + '\\Python\\Cours_openclassroom\\forum\\data'
    if current_path != dest_path:
        os.chdir(dest_path)

    if obj__repr__ not in dest_list:
        with open(file_csv, "a", newline='', encoding='utf-8') as file:
            data_a = csv.writer(file, delimiter=',')
            data_a.writerow(obj__repr__)
    os.chdir(current_path)

def init_data_user():  # initialise la récupération des données du fichier data.csv
    extract_data_csv('\\Python\\Cours_openclassroom\\forum\\data', 'data_user.csv', ["name", "pass", "status", "autority"], pac.Shell.list_user)

def init_obj_user():  # recréé une liste d'objet user dans le shell
    for data_user in pac.Shell.list_user:
        if data_user != None:
            obj = get_user_csv(data_user)
            pac.Shell.list_obj_user.append(obj)

def get_user_csv(obj_list_user_csv):  # récupère le __repr__ de l'objet non-instancié du fichier data_user.csv et recréé l'instance de cet objet.
    index = pac.Shell.list_user.index(obj_list_user_csv)
    try:
        pac.Shell.list_user[index][3] 
        if pac.Shell.list_user[index][3] == 'Admin':
            return pac.Admin(pac.Shell.list_user[index][0], pac.Shell.list_user[index][1], pac.Shell.list_user[index][2])
        elif pac.Shell.list_user[index][3] == 'Modo':
            return pac.Moderateur(pac.Shell.list_user[index][0], pac.Shell.list_user[index][1], pac.Shell.list_user[index][2])
    except IndexError:
        return pac.User(pac.Shell.list_user[index][0], pac.Shell.list_user[index][1], pac.Shell.list_user[index][2])

#-------------------------------------------------Fonctions lié à la class Thread------------------------------------------------------------

