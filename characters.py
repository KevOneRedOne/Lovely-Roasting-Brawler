'''
Creation d'une classe regroupant tous les personnages jouables par les joueurs
'''
class Characters:
    def __str___(self):
        return "Le personnage s'appelle" + self.name + self.adjective 

    def __init__(self, name) :
        if name == "Bryan":
            self.name = "Bryan"
            self.adjective = "Le gamin énervant !"
            self.health = 100
            self.faiblesse = []
        elif name == "Francis":
            self.name = "Francis"
            self.adjective = "Le vieux !"
            self.health = 100 
            self.faiblesse = []
        elif name == "Jean-Michel":
            self.name = "Jean-Michel"
            self.adjective = "Le grincheux susceptible !"
            self.health = 100 
            self.faiblesse = []
        elif name == "Martha":
            self.name = "Martha"
            self.adjective = "Championne UFC"
            self.health = 100 
            self.faiblesse = []
        elif name == "Agnès":
            self.name = "Agnès"
            self.adjective = "La naïve"
            self.health = 100 
            self.faiblesse = []

