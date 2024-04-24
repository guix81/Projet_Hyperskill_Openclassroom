import requests
from bs4 import BeautifulSoup
import csv



list_content = []
with open('Python\\Projet_openclassroom\\Projet_openclassroom_2\\input.csv', 'r', encoding='utf-8') as file:
    read_file = csv.DictReader(file, delimiter=',')
    for i in read_file:
        list_content.append(i)

for i in range(len(list_content)):
    list_content[i]['heures_travaillees'] = int(list_content[i]['heures_travaillees'].lstrip('\t'))
    list_content[i]['heures_travaillees'] = str(list_content[i]['heures_travaillees'] * 15)
    
head = []
for i in list_content[0].keys():
    head.append(i)

content = []
for x in range(len(list_content)):
    list_ = []
    for key in list_content[x].keys():
        list_.append(list_content[x][key])
    content.append(list_)

with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    file_export = csv.writer(file, delimiter=',')
    file_export.writerow(head)
    for i in range(len(content)):
        file_export.writerow(content[i])
















