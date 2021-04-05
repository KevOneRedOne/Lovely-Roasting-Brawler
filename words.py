'''

Creation d'une classe regroupant tous les mots disponibles ! 

'''
class Sujet:
    def __str__(self):
        return "coucou"

    def __init__(self):
        self.listeSujet = [
            "Mon chien","Votre mère","Mes chaussettes","Le président des Etats-Unis","Le Maire"
        ]

    def listeWord(self):
        for mot in self.listeSujet:
            print(mot)

# class Verbe:
#     def __str___(self):
#         return self.listeVerbe 

#     def __init__(self):
#         self.listeVerbe = [
#             "Est parti","A lavé","était","sont"
#         ]

# class Complement:
#     def __init__(self):
#         self.listeComplement= [
#             "Ce soir","à l'école","La semaine dernière"
#         ]

# class Liaisons:
#     def __init__(self):
#         self.listeLiaisons = [
#             "et","car","en d'autres termes","par ailleurs","sans compter que","mais", "où","donc","or"
#         ]

# class FinDePhrase:
#     def __init__(self):
#         self.listeFinDePhrase = [
#             "Et tout le monde le sait !","Et bim !","Tu peux pas le nier"
#         ]