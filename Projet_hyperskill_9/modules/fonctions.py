class CafeMachine:
    reserve_money = 550
    reserve_cafe = 120
    reserve_lait = 540
    reserve_eau = 400
    reserve_gobelet = 9

    def __init__(self):
        pass

    def verification(self, obj):  # vérifie si la machine possède les fournitures nécessaire
        if obj.cafe <= self.reserve_cafe:
            if obj.lait <= self.reserve_lait:
                if obj.eau <= self.reserve_eau:
                    if obj.gobelet <= self.reserve_gobelet:
                        return True
                    
    def make_cafe(self, obj):  # action: fait le café (déduit les fournitures et encaisse l'argent)
        self.reserve_cafe -= obj.cafe
        self.reserve_lait -= obj.lait
        self.reserve_eau -= obj.eau
        self.reserve_gobelet -= obj.gobelet
        self.reserve_money += obj.prix
        self.display()

    def fill(self):
        self.reserve_eau += int(input('Write how many ml of water you want to add:\n'))
        self.reserve_lait += int(input('Write how many ml of milk you want to add:\n'))
        self.reserve_cafe += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.reserve_gobelet += int(input('Write how many disposable cups you want to add:\n'))
        print('')
        self.display()

    def take(self):
        print(f'I gave you ${self.reserve_money}')
        self.reserve_money -= self.reserve_money
        print('')
        self.display()
    
    def display(self):
        print('The coffee machine has:')
        print(f'{self.reserve_eau} ml of water')
        print(f'{self.reserve_lait} ml of milk')
        print(f'{self.reserve_cafe} g of coffee beans')
        print(f'{self.reserve_gobelet} disposable cups')
        print(f'${self.reserve_money} of money\n')


class Expresso(CafeMachine):
    def __init__(self):
        self.cafe = 16 # graine de café en gramme pour une tasse
        self.eau = 250  # en ml pour une tasse
        self.prix = 4  # prix en dollar
        self.lait = 0  # en ml pour une tasse
        self.gobelet = 1 
    
class Latte(CafeMachine):
    def __init__(self):
        self.cafe = 20 
        self.eau = 350  
        self.prix = 7  
        self.lait = 75  
        self.gobelet = 1 
    
class Cappuccino(CafeMachine):
    def __init__(self):
        self.cafe = 12 
        self.eau = 200  
        self.prix = 6  
        self.lait = 100   
        self.gobelet = 1 
    
def decision(machine_cafe):  # argument = obj 
    rep = input('Write action (buy, fill, take):\n')
    if rep == 'buy':
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if choice == '1':
            cafe = Expresso()
            if machine_cafe.verification(cafe):
                machine_cafe.make_cafe(cafe)
        elif choice == '2':
            cafe = Latte()
            if machine_cafe.verification(cafe):
                machine_cafe.make_cafe(cafe)
        elif choice == '3':
            cafe = Cappuccino()
            if machine_cafe.verification(cafe):
                machine_cafe.make_cafe(cafe)
    elif rep == 'fill':
        machine_cafe.fill()
    elif rep == 'take':
        machine_cafe.take()