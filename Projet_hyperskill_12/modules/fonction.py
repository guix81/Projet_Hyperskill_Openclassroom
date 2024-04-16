import random
import os
import  sys


class Ring:
    list_obj = ('scissors', 'paper', 'rock',)  # objet par defaut
    ref_option = ('rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'lizard', 'spock',)
    def __init__(self):
        self.list_chaine = ''
        self.base_score = {}
        self.dic = {}
        self.list_option = []

    def verif(self, obj_1, obj_2, player):  # vérifie l'objet choisi par le joueur et le bot et les compare
        if obj_1.OBJET in obj_2.FAIBLE:
            self.base_score[player.player_name] = str(int(self.base_score[player.player_name]) + 100)
            self.write_result('rating.txt')
            return f'Well done. The computer chose {self.result_bot.OBJET} and failed'
        elif obj_1.OBJET in obj_2.FORCE:
            return f'Sorry, but the computer chose {self.result_bot.OBJET}'
        else:
            self.base_score[player.player_name] = str(int(self.base_score[player.player_name]) + 50)
            self.write_result('rating.txt')
            return f'There is a draw ({self.result_bot.OBJET})'
        
    def calc(self, obj_player, player, instance_ring):  # génère la décision du bot et l'intègre dans la méthode verif()
        self.obj_player = obj_player
        self.player = player
        bot = Bot()
        self.result_bot = bot.decision(instance_ring)
        x = self.verif(obj_player, self.result_bot, player)
        return x
    
    def read_file(self, file):  # lis le fichier rating.txt et extrait sous forme de liste les éléments
        self.file = file
        if file not in os.listdir('.'):
            fichier = open(file, 'w')
            fichier.close()
        else:
            fichier = open(file, 'r')
            for i in fichier.read(-1):
                self.list_chaine = self.list_chaine + i
            fichier.close()
            if self.list_chaine != '':
                self.list_chaine = self.list_chaine.split('\n')

    def your_rating(self, player):
        print('Your rating: ' + str(self.base_score[player.player_name]))

    def write_init(self, file, player_obj):  # ajoute les nouveaux joueurs
        self.file = file
        self.player_obj = player_obj
        fichier = open(file, 'a')
        fichier.write(player_obj.player_name + ' ' + str(player_obj.score) + '\n')
        fichier.close()

    def write_result(self, file):
        fichier = open(file, 'w')
        for i in self.base_score.items():
            x = i[0]
            y = i[1]
            fichier.write(x + ' ' + y + '\n')
        fichier.close()

    def analyse_file(self):  # analyse la liste des éléments fournie par read_file() et les stockes dans un dictionnaire (base_score)
        list_dict = []
        for i in range(len(self.list_chaine)):
            list_dict.append(self.list_chaine[i].split(" "))
        for x in range(len(list_dict)):
            self.base_score.update({list_dict[x][0] : list_dict[x][-1]})

    def reanalyse(self, player):  # met à jour le dictionaire pour le nouveau joueur
        self.dic.update({player.player_name : player.score})
        self.base_score.update(self.dic)
        
class Bot(Ring):
    def __init__(self):
        pass

    def decision(self, instance_ring):
        random.seed(random.randint(1, 100))
        if instance_ring.list_option == []:
            choix = random.choice(Ring.list_obj)  # choix par defaut
        else:
            choix = random.choice(instance_ring.list_option)
        if choix == 'scissors':
            return Ciseau()
        elif choix == 'rock':
            return Pierre()
        elif choix == 'paper':
            return Feuille()
        elif choix == 'gun':
            return Gun()
        elif choix == 'lightning':
            return Lightning()
        elif choix == 'devil':
            return Devil()
        elif choix == 'dragon':
            return Dragon()
        elif choix == 'water':
            return Water()
        elif choix == 'air':
            return Air()
        elif choix == 'sponge':
            return Sponge()
        elif choix == 'wolf':
            return Wolf()
        elif choix == 'tree':
            return Tree()
        elif choix == 'human':
            return Human()
        elif choix == 'snake':
            return Snake()
        elif choix == 'fire':
            return Fire()
        elif choix == 'spock':
            return Spock()
        elif choix == 'lizard':
            return Lizard()
        

class Player(Ring):
    def __init__(self, name, score):
        self.player_name = name
        self.score = score

class Ciseau(Ring):
    OBJET = 'scissors'
    FORCE = 'snake human tree wolf sponge paper air'
    FAIBLE = 'rock fire gun lightning devil dragon water lizard spock'

class Pierre(Ring):
    OBJET = 'rock'
    FORCE = 'fire scissors snake human tree wolf sponge lizard spock'
    FAIBLE = 'paper gun lightning devil dragon water air'
    
class Feuille(Ring):
    OBJET = 'paper'
    FORCE = 'rock gun lightning devil dragon water air spock'
    FAIBLE = 'fire scissors snake human tree wolf sponge lizard'

class Gun(Ring):
    OBJET = 'gun'
    FORCE = 'wolf tree human snake scissors fire rock'
    FAIBLE = 'lightning devil dragon water air paper sponge'

class Lightning(Ring):
    OBJET = 'lightning'
    FORCE = 'gun rock fire scissors snake human tree'
    FAIBLE = 'devil dragon water air paper sponge wolf'

class Devil(Ring):
    OBJET = 'devil'
    FORCE = 'gun rock fire scissors snake human lightning'
    FAIBLE = 'dragon water air paper sponge wolf tree'

class Dragon(Ring):
    OBJET = 'dragon'
    FORCE = 'gun rock fire scissors snake lightning devil'
    FAIBLE = 'water air paper sponge wolf tree human'

class Water(Ring):
    OBJET = 'water'
    FORCE = 'gun rock fire scissors lightning devil dragon'
    FAIBLE = 'air paper sponge wolf tree human snake'

class Air(Ring):
    OBJET = 'air'
    FORCE = 'gun rock fire lightning devil dragon water'
    FAIBLE = 'paper sponge wolf tree human snake scissors'
    
class Sponge(Ring):
    OBJET = 'sponge'
    FORCE = 'gun lightning devil dragon water air paper'
    FAIBLE = 'fire scissors snake human tree wolf rock'

class Wolf(Ring):
    OBJET = 'wolf'
    FORCE = 'lightning devil dragon water air paper sponge'
    FAIBLE = 'fire scissors snake human tree rock gun'

class Tree(Ring):
    OBJET = 'tree'
    FORCE = 'devil dragon water air paper sponge wolf'
    FAIBLE = 'fire scissors snake human rock gun lightning'

class Human(Ring):
    OBJET = 'human'
    FORCE = 'dragon water air paper sponge wolf tree'
    FAIBLE = 'fire scissors snake rock gun lightning devil'

class Snake(Ring):
    OBJET = 'snake'
    FORCE = 'water air paper sponge wolf tree human'
    FAIBLE = 'fire scissors rock gun lightning devil dragon'

class Fire(Ring):
    OBJET = 'fire'
    FORCE = 'snake human tree wolf sponge paper scissors'
    FAIBLE = 'rock gun lightning devil dragon water air'

class Lizard(Ring):
    OBJET = 'lizard'
    FORCE = 'scissors paper'
    FAIBLE = 'spock rock'

class Spock(Ring):
    OBJET = 'spock'
    FORCE = 'lizard scissors'
    FAIBLE = 'rock paper'

def jeu_defaut(instance_ring, player):
    while True:
        choix = input()
        if choix in Ring.list_obj:
            if choix == 'scissors':
                obj = Ciseau()
            elif choix == 'rock':
                obj = Pierre()
            elif choix == 'paper':
                obj = Feuille()
            print(instance_ring.calc(obj, player, instance_ring))
        elif choix == '!exit':
            print('Bye!')
            sys.exit(1)
        elif choix == '!rating':
            instance_ring.your_rating(player)
        else:
            print('Invalid input')

def jeu_custom(instance_ring, player):
    while True:
        choix = input()
        if choix in instance_ring.list_option:
            if choix == 'scissors':
                obj = Ciseau()
            elif choix == 'rock':
                obj = Pierre()
            elif choix == 'paper':
                obj = Feuille()
            elif choix == 'gun':
                obj = Gun()
            elif choix == 'lightning':
                obj = Lightning()
            elif choix == 'devil':
                obj = Devil()
            elif choix == 'dragon':
                obj = Dragon()
            elif choix == 'water':
                obj = Water()
            elif choix == 'air':
                obj = Air()
            elif choix == 'sponge':
                obj = Sponge()
            elif choix == 'wolf':
                obj = Wolf()
            elif choix == 'tree':
                obj = Tree()
            elif choix == 'human':
                obj = Human()
            elif choix == 'snake':
                obj = Snake()
            elif choix == 'fire':
                obj = Fire()
            elif choix == 'lizard':
                obj = Lizard()
            elif choix == 'spock':
                obj = Spock()
            print(instance_ring.calc(obj, player, instance_ring))
        elif choix == '!exit':
            print('Bye!')
            sys.exit(1)
        elif choix == '!rating':
            instance_ring.your_rating(player)
        else:
            print('Invalid input')