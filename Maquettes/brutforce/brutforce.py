import itertools
import string

"""Méthode de brutforce synchrone"""

class Brutforce():
    d = string.digits
    l = string.ascii_letters
    p = string.printable
    

    @classmethod
    def crack_pass(cls, *arg, len_max=3):  # *args : liste de chaine de caractère utilisé par le brutforce, len_max : taille max du mot de pass.
        lst = []
        iti = set(itertools.chain(*arg))
        for _ in range(len_max):
            lst.append(iti)
        
        for i in itertools.product(*lst):
                print(i)  # remplacer cette fonction pour une sortie approprier (exemple: un champs de mot de pass d'un site internet ou d'une application)

"""
exemple:

Brutforce.crack_pass(Brutforce.d, Brutforce.l, Brutforce.p, len_max=3)

"""