class Tool:
    def __init__(self, name):
        self.name = name

class ToolBox:
    def __init__(self):
        self.tool = []

    def add_tool(self, tool):
        self.tool.append(tool)

    def del_tool(self, tool):
        index = self.tool.index(tool)
        del self.tool[index]

    def inventaire(self):
        for i in self.tool:
            print(i.__repr__())


class Marteau(Tool):
    def __init__(self, name, color='marron'):
        self.name = name
        self.color = color

    def change_color(self, color):
        self.color = color

    def clou_in(self):
        Clou.clou_in()
        print('Je plante un clou!')

    def clou_out(self):
        Clou.clou_out()
        print('Je retire un clou!')

    def __repr__(self):
        return self.name + ' | ' + self.color
        

class Tournevis:
    def __init__(self, name, taille):
        self.name = name
        self.taille = taille

    def serrer_vis(self):
        Vis.serrage()
        print('Je serre la vis!')

    def desserrer_vis(self):
        Vis.desserrage()
        print('Je desserre la vis!')

    def __repr__(self):
        return self.name + ' | ' + self.taille + ' mm'
    

class Vis:
    MAX_FORCE_SERRAGE = 5
    def __init__(self, name, force=3):
        self.name = name
        self.force = force

    def serrage(self):
        self.force += 1

    def desserrage(self):
        self.force -=1

    def __str__(self):
        return f"la vis '{self.name}' à un serrage de force {str(self.force)}"
    
class Clou:
    def __init__(self, name, etat='out'):
        self.name = name
        self.etat = etat

    def clou_in(self):
        self.etat = 'in'
        print(f"le clou '{self.name}' est planté dans le mur")

    def clou_out(self):
        self.etat = 'out'
        print(f"le clou '{self.name}' est retiré du mur")

    def __str__(self):
        etat = " est planté dans le mur." if self.etat == 'in' else " est retiré du mur."
        return f"Le clou '{self.name}'" + etat


