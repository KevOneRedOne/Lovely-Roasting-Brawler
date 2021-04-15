'''
Creation d'une classe regroupant tous les personnages jouables par les joueurs
'''
class Characters:
    def __init__(self, name) :
        if name == "Bryan":
            self.name = "Bryan"
            self.adjective = "Le gamin énervant !"
            self.health = 100
            self.faiblesse = ["Ton père ",
            "Un écolier effrayé ",
            "Un bouffon ",
            "Un jeune homme sans défense ",
            "n'est pas intéréssant ",
            "est encore un gamin ",
            "parle aux inconnus ",
            "Espèce de gros noob !"
            "Espèce d'avorton !"]
        elif name == "Francis":
            self.name = "Francis"
            self.adjective = "Le vieux."
            self.health = 100
            self.faiblesse = ["Un vieux croûton paresseux ",
            "Un vieux débris ",
            "est un vieux bougre ",
            "est vieux ",
            "est une pierre morte",
            "a aucune expérience de la vie",
            "n'a pas de télé en couleur ",
            "Vieux schnock !"]
        elif name == "Jean-Michel":
            self.name = "Jean-Michel"
            self.adjective = "Possède un égo surdimensionné"
            self.health = 100
            self.faiblesse = ["Un blazer par cher ",
            "Un malotru ",
            "Un mafieu enragé",
            "Ce pauvre monsieur ",
            "n'est pas sérieux",
            "est rayé",
            "est sans valeur",
            "ne peut pas acheter un escalier jusqu'au paradis ",
            "est habitué a voler a des orphelins ",
            "Comme un paysan répugnant !"]
        elif name == "Martha":
            self.name = "Martha"
            self.adjective = "La championne UFC."
            self.health = 100
            self.faiblesse = ["Une truie grognieuse ",
            "Imbécile",
            "est aussi salé qu'un joueur de League Of Legends ",
            "Une femme bizarre allongée sur un étang",
            "devrait être dans une cage ",
            "rammène des insultes a un combat d'épée ",
            "se déplace comme une vache enceinte ",
            "Gros naze !"]
        elif name == "Agnès":
            self.name = "Agnès"
            self.adjective = "La fashion victime."
            self.health = 100
            self.faiblesse = ["Ton chapeau ",
            "Ton sens de la mode ",
            "Les chausettes d'un sans abris ",
            "n'est pas ma création ",
            "met des vêtements de grand-mère ",
            "porte des vêtements de seconde main ",
            "a des cheuveux plus nuls que ",
            "Maintenant met une chaussette par dessus !"]

    def __str___(self):
        return "Le personnage s'appelle" + self.name + self.adjective 
