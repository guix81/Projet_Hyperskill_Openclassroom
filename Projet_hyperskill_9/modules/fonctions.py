import math

class CafeMachine:
    G_CAFE = 15 # graine de café en gramme pour une tasse
    LAIT = 50  # en ml pour une tasse
    EAU = 200  # en ml pour une tasse
    def __init__(self):
        pass

    def make_cafe(self):  # fait un café
        print('''Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!''')
        
    def n_cafe_need(self):  # déternime la réserve des matières première par rapport au nombre de tasse café
        rep = input('Write how many cups of coffee you will need:\n')
        eau = CafeMachine.EAU * int(rep)
        lait = CafeMachine.LAIT * int(rep)
        g_cafe = CafeMachine.G_CAFE * int(rep)
        print(f'''For {rep} cups of coffee you will need:
{eau} ml of water
{lait} ml of milk
{g_cafe} g of coffee beans''')
        
    def capacity(self):  # détermine le nombre de tasse de café par rapport à la réserve des matières première
        ml_eau = int(input('Write how many ml of water the coffee machine has:\n'))
        ml_lait = int(input('Write how many ml of milk the coffee machine has:\n'))
        g_cafe = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
        n_cafe = int(input('Write how many cups of coffee you will need:\n'))
        tq_eau = math.floor(ml_eau / CafeMachine.EAU)
        tq_lait = math.floor(ml_lait / CafeMachine.LAIT)
        tq_cafe = math.floor(g_cafe / CafeMachine.G_CAFE)
        result = [tq_eau, tq_lait, tq_cafe]
        n_tasse = min(result)
        if n_tasse >= n_cafe:
            if n_tasse == n_cafe:
                print('Yes, I can make that amount of coffee')
            else:
                n_tasse = n_tasse - n_cafe
                print('Yes, I can make that amount of coffee' + f' (and even {n_tasse} more than that)')
        elif n_cafe > n_tasse:
            print(f'No, I can make only {n_tasse} cups of coffee')
        else:
            print('No, I can make only 0 cups of coffee')
