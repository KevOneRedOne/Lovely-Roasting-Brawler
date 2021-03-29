'''

Creation d'une classe regroupant tous les mots disponibles ! 

'''
class Sujet:
    def __init__(self):
        self.liste = [
            "Mon chien","Votre mère","Mes chaussettes"
        ]

            


class Verbe:
    def __init__(self):
        self.liste= [
            "Est parti","A lavé","était","sont"
        ]

class Complement:
    def __init__(self):
        self.liste= [
            "Ce soir","à l'école","La semaine dernière"
        ]

class Liaisons:
    def __init__(self):
        self.liste = [
            "et","car","en d'autres termes","par ailleurs","sans compter que"
        ]

class FinDePhrase:
    def __init__(self):
        self.liste = [
            "Et tout le monde le sait !","Et bim !","Tu peux pas le nier"
        ]