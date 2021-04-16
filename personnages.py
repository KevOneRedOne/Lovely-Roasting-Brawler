'''
Création d'une classe regroupant tous les personnages jouables par les joueurs et contient toutes les informations liées à notre personnage.
'''
# 
class Personnages:
    def __str__(self):
        return self.nom + ", " + self.adjectif + " " + self.description

    def __init__(self, nom):
        if nom == "Bryan":
            self.nom = "Bryan"
            self.adjectif = "Le gamin énervant !"
            self.description = "Il n'aime pas que l'on parle de ses parents, et qu'on le traite de gamin."
            self.faiblesse = ["Ton père",
            "Un écolier effrayé",
            "Un bouffon",
            "Un jeune homme sans défense",
            "n'est pas intéréssant",
            "est encore un gamin",
            "parle aux inconnus",
            "Espèce de gros noob !"
            "Espèce d'avorton !"]
            
        elif nom == "Francis":
            self.nom = "Francis"
            self.adjectif = "Le vieux."
            self.description = "Il ne supporte pas sa vieillesse..."
            self.faiblesse = ["Un vieux croûton paresseux.",
            "Un vieux débris",
            "est un vieux bougre",
            "est vieux",
            "est une pierre morte",
            "a aucune expérience de la vie",
            "n'a pas de télé en couleur ",
            "Vieux schnock !"]

        elif nom == "Jean-Michel":
            self.nom = "Jean-Michel"
            self.adjectif = "possède un égo surdimensionné"
            self.description = "et il n'aime pas qu'on le rabaisse !"
            self.faiblesse = ["Un blazer par cher",
            "Un malotru",
            "Un mafieu enragé",
            "Ce pauvre monsieur",
            "n'est pas sérieux",
            "est rayé",
            "est sans valeur",
            "ne peut pas acheter un escalier jusqu'au paradis",
            "est habitué a voler a des orphelins",
            "Comme un paysan répugnant !"]

        elif nom == "Martha":
            self.nom = "Martha"
            self.adjectif = "La championne UFC."
            self.description = "Elle réagit au quart de tour !"
            self.faiblesse = ["Une truie grognieuse",
            "Imbécile",
            "est aussi salé qu'un joueur de League Of Legends",
            "Une femme bizarre allongée sur un étang",
            "devrait être dans une cage",
            "rammène des insultes a un combat d'épée",
            "se déplace comme une vache enceinte",
            "Gros naze !"]

        elif nom == "Agnès":
            self.nom = "Agnès"
            self.adjectif = "La fashion victime."
            self.description = "Elle n'aime qu'on critique son sens de la mode !"
            self.faiblesse = ["Ton chapeau",
            "Ton sens de la mode",
            "Les chausettes d'un sans abris",
            "n'est pas ma création",
            "met des vêtements de grand-mère",
            "porte des vêtements de seconde main",
            "a des cheuveux plus nuls que",
            "Maintenant met une chaussette par dessus !"]