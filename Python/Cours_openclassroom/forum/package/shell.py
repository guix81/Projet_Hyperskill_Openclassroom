from abc import ABC

class Shell(ABC):
    list_user = []  # une liste de liste des données utilisateur sous forme de [name, pass, status, autority] venant du fichier data_user.csv
    list_obj_user = []
    list_posts = []  # List d'objet de class Post
    list_obj_post = []
    list_threads = []
    list_obj_thread = []
    path_data = ""