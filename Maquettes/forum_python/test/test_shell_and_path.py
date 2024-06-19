import os
import package as pac


def test_shell_const():  # Test des constantes.
    assert pac.Shell.csv_files == ("data_user.csv", "data_posts.csv", "data_threads.csv")
    assert pac.Shell.head_user == ("name", "mdp", "status", "id", "autority")
    assert pac.Shell.head_post == ("content_post", "username_post", "date_post", 'id')
    assert pac.Shell.head_thread == ("title_thread", "username_thread", "date_trhead", "id", "liste_id_post")
    assert pac.Shell.path_data == "\\Maquettes\\forum_python\\data"
    
def test_existance_path():  # test de l'existance des chemins des fichiers csv.
        assert os.path.exists(os.getcwd() + pac.Shell.path_data) == True

        for file in pac.Shell.csv_files:
            assert os.path.exists(os.getcwd() + pac.Shell.path_data + '\\' + file) == True