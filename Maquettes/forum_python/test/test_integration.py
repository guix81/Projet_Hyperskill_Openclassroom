import package as pac


def test_integration_shell_lst():  # Test l'extraction des datas.
    for shell_lst, file_csv, shell_head in zip(pac.Shell.lsts, pac.Shell.csv_files, pac.Shell.heads):
        assert pac.extract_data_csv(pac.Shell.path_data, file_csv, shell_head, shell_lst) == True

def test_integration_obj():  # Test la recréation des objets à partir de la data extraite.
    assert pac.fonctions.init_obj_user() == True
    assert pac.fonctions.init_obj_post() == True
    assert pac.fonctions.init_obj_thread() == True


