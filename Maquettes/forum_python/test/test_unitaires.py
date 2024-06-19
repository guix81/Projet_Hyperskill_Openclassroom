import pytest
import package as pac


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
    #je vérifie la présence des représentation des trois objet sous forme de dictionnaire dans list_user
    for i in [obj_1, obj_2, obj_3]:
        assert i.__repr__() in pac.Shell.list_user

@pytest.mark.parametrize("shell_obj, res", zip([obj_1, obj_2, obj_3], [True, True, True]))  
def test_modif_data(shell_obj, res):
    # suppression des trois comptes.
    assert pac.modif_database(shell_obj, pac.Shell.list_obj_user, 'data_user.csv', pac.Shell.head_user, mode='del') is res