import pytest
import os
import package as pac

#----------------------------------------------------------------------modif_database----------------------------------------------------------------------------------
# Je créé trois comptes, un de chaque type différent.
obj_1 = pac.User('testUser', 'testPass')
obj_2 = pac.Admin('testAdmin', 'testPass')
obj_3 = pac.Moderateur('testModo', 'testPass')

def test_presence_obj_user_in_lst():
    # Je vérifie la présence des trois objets dans list_obj_user
    lst = []
    for x in pac.Shell.list_obj_user:
        lst.append(id(x))
    for i in [obj_1, obj_2, obj_3]:
        assert id(i) in lst

def test_presence_data_user_in_lst():
    # je vérifie la présence des représentations des trois objets sous forme de dictionnaire dans list_user
    for i in [obj_1, obj_2, obj_3]:
        assert i.__repr__() in pac.Shell.list_user

@pytest.mark.parametrize("shell_obj, res", zip([obj_1, obj_2, obj_3], [True, True, True]))  
def test_modif_data_1(shell_obj, res):
    # suppression des trois comptes.
    assert pac.modif_database(shell_obj, pac.Shell.list_obj_user, 'data_user.csv', pac.Shell.head_user, mode='del') is res

# je créé un thread et un post.
post = pac.Post("texte test", 'guix')
thread = pac.Thread("title test", 'guix')

def test_presence_data_in_file_post_1():
    # je vérifie la présence de la data dans le fichier data_posts.csv.
    assert pac.fonctions.verif_data("data_posts.csv", post) is True

def test_presence_data_in_file_thread_1():
    # je vérifie la présence de la data dans le fichier data_threads.csv.
    assert pac.fonctions.verif_data("data_threads.csv", thread) is True

@pytest.mark.parametrize("obj, list_obj, file_csv, head, key, val, res", zip([post, thread], 
                                                                        [pac.Shell.list_obj_post, pac.Shell.list_obj_thread], 
                                                                        ["data_posts.csv", "data_threads.csv"], 
                                                                        [pac.Shell.head_post, pac.Shell.head_thread], 
                                                                        ["content_post", "title_thread"], 
                                                                        ["new text test", "new title test"], 
                                                                        [True, True]))  
def test_modif_data_2(obj, list_obj, file_csv, head, key, val, res):
    # modification de la database du fichier "data_posts.csv" & "data_threads.csv" sous forme de paire clé-valeur.
    assert pac.modif_database(obj, list_obj, file_csv, head, key=key, value=val, mode='modif_val') is res

def test_presence_data_in_file_post_2():
    # je vérifie la modification de la data dans le fichier data_posts.csv.
    assert pac.fonctions.verif_data("data_posts.csv", post) is True

def test_presence_data_in_file_thread_2():
    # je vérifie la modification de la data dans le fichier data_threads.csv.
    assert pac.fonctions.verif_data("data_threads.csv", thread) is True

@pytest.mark.parametrize("obj, list_obj, file_csv, head, res", zip([post, thread], 
                                                                   [pac.Shell.list_obj_post, pac.Shell.list_obj_thread], 
                                                                   ["data_posts.csv", "data_threads.csv"], 
                                                                   [pac.Shell.head_post, pac.Shell.head_thread],  
                                                                   [True, True]))
def test_modif_data_3(obj, list_obj, file_csv, head, res):
    # Suppression des objets Post et Thread.
    assert pac.modif_database(obj, list_obj, file_csv, head, mode='del') is res

def test_presence_data_in_file_post_3():
    # je vérifie la suppression de la data dans le fichier data_posts.csv.
    assert pac.fonctions.verif_data("data_posts.csv", post) is False

def test_presence_data_in_file_thread_3():
    # je vérifie la suppression de la data dans le fichier data_threads.csv.
    assert pac.fonctions.verif_data("data_threads.csv", thread) is False
