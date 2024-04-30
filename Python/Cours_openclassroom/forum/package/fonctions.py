import os
import csv
import package as pac


def tuple_to_list(super_f, autority):
    x = []
    for i in super_f:
        x.append(i)
    x.append(autority)
    return x

#-------------------------------------------------Fonctions lié à la class User--------------------------------------------------------------

def maj_data_user(obj__repr__):  # Ajoute le __repr__ de l'objet User dans le fichier data.
    pac.Shell.list_user.clear()
    init_data_user()

    if obj__repr__ not in pac.Shell.list_user:
        with open("data_user.csv", "a", newline='', encoding='utf-8') as file:
            data_a = csv.writer(file, delimiter=',')
            data_a.writerow(obj__repr__)

def get_user_csv(obj_list_user_csv):
    index = pac.Shell.list_user.index(obj_list_user_csv)
    try:
        pac.Shell.list_user[index][3] 
        if pac.Shell.list_user[index][3] == 'Admin':
            return pac.Admin(pac.Shell.list_user[index][0], pac.Shell.list_user[index][1], pac.Shell.list_user[index][2])
        elif pac.Shell.list_user[index][3] == 'Modo':
            return pac.Moderateur(pac.Shell.list_user[index][0], pac.Shell.list_user[index][1], pac.Shell.list_user[index][2])
    except IndexError:
        return pac.User(pac.Shell.list_user[index][0], pac.Shell.list_user[index][1], pac.Shell.list_user[index][2])

def init_data_user():  # initialise la récupération des données du fichier data.csv
    current_path = os.getcwd()
    if pac.Shell.path_data != os.getcwd():
        pac.Shell.path_data = os.getcwd() + '\\Python\\Cours_openclassroom\\forum\\data'
        os.chdir(pac.Shell.path_data)

    if "data_user.csv" not in os.listdir('.'):  # Si le fichier n'existe pas, il sera créé avec une en-tête.
        with open("data_user.csv", "w", newline='', encoding='utf-8') as file:
            data_w = csv.writer(file, delimiter=',')
            data_w.writerow(["name", "pass", "status", "autority"])
    
    with open("data_user.csv", "r", newline='', encoding='utf-8') as file:  # Lecture du fichier data pour récupérer les données dans le shell.
        data_r = csv.reader(file, delimiter=',')
        for i in data_r:
            pac.Shell.list_user.append(i)
    
    os.chdir(current_path)

def init_obj_user():
    for data_user in pac.Shell.list_user:  # recréé une liste d'objet user dans le shell
        if data_user != None:
            obj = get_user_csv(data_user)
            pac.Shell.list_obj_user.append(obj)

