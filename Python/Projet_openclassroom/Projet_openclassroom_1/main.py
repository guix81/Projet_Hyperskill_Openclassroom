from bs4 import BeautifulSoup


class Produit:
    def __init__(self, name, prix, descript):
        self.name = name
        self.prix = prix
        self.descript = descript


file = open('Python\Projet_openclassroom\Projet_openclassroom_1\index.html', 'r', encoding='utf-8')
soup = BeautifulSoup(file, 'html.parser')

titre = soup.title
print(titre)

h1 = soup.find("h1")
print(h1)

list_obj = []
list_nom = []
list_prix = []
list_descript = []

nom_prod = soup.find_all("h2")
print(nom_prod)
nom_prod = list(nom_prod)
for i in range(len(nom_prod)):
    chaine = str(nom_prod[i])
    chaine = chaine.lstrip('<h2>')
    chaine = chaine.replace('</h2>', '')
    list_nom.append(chaine)

prix_descrip = soup.find_all("p")
print(prix_descrip)
prix_descrip = list(prix_descrip)
for i in range(1, len(prix_descrip), 2):
    chaine = str(prix_descrip[i])
    chaine = chaine.lstrip('<p>Prix : ')
    chaine = chaine.replace('</p>', '')
    list_prix.append(chaine)

file.close()

for i in range(0, len(prix_descrip), 2):
    chaine = str(prix_descrip[i])
    chaine = chaine.lstrip('<p>Description : ')
    chaine = chaine.replace('</p>', '')
    list_descript.append(chaine)
list_descript.pop(0)

for i in range(len(nom_prod)):
    inst_obj = Produit(list_nom[i], list_prix[i], list_descript[i])
    list_obj.append(inst_obj)

for i in range(len(list_obj)):
    list_obj[i].prix = list_obj[i].prix.rstrip('€')
    list_obj[i].prix = int(list_obj[i].prix) * 1.2
    list_obj[i].prix = str(list_obj[i].prix) + '$'

for i in range(len(list_obj)):
    print(list_obj[i].name + ' ' + list_obj[i].prix + ' ' + list_obj[i].descript)