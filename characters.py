'''
Creation d'une classe regroupant tous les personnages jouables par les joueurs
'''
class Characters:
    def __str___(self):
        return "Le personnage choisi est " + self.type

    def __init__(self, type) :
        if type == "Perso1":
            self.type = "Perso1"
            self.health = 100
        elif type == "Perso2":
            self.type = "Perso2"
            self.health = 100 
        elif type == "Perso3":
            self.type = "Perso3"
            self.health = 100 
        elif type == "Perso4":
            self.type = "Perso4"
            self.health = 100 
