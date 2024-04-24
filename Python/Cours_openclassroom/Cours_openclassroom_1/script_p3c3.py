import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"

def extraction_html(url):  # extraction code html en bytes
    reponse = requests.get(url)
    page = reponse.content
    return page

def transformation(content):  # conversion de l'extraction en un objet avec des méthodes pour trouver les éléments
    soup = BeautifulSoup(content, "html.parser")
    return soup

def recuperation(objet_soup):  # récupération des titres et des descriptions par l'objet soup
    elements = objet_soup.find_all("li", class_="gem-c-document-list__item")
    print(elements)
    resultats = []
    for element in elements:
        titre = element.find("a", class_="govuk-link")
        description = element.find("p", class_="gem-c-document-list__item-description")
        donnee = [titre.string, description.string]
        resultats.append(donnee)
    return resultats
        
def exportation_cvs(resultats):
    en_tete = ["titre", "description"]
    with open("data.csv", "w", newline="", encoding="utf-8") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=",")
        writer.writerow(en_tete)
        for donnee in resultats:
            writer.writerow(donnee)


         
content = extraction_html(url)
soup = transformation(content)
resultat = recuperation(soup)
exportation_cvs(resultat)










