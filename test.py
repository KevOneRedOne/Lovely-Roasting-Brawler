import random
from listedemots import List1,List2,List3,List4,List5

print("Grille Principale :")
def MainGridGenerator() :
    Grille10Mots = []
    i = 0
    while i < 10:
        Grille10Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(Grille10Mots)
MainGridGenerator()

print("Grille Joueur 1 :")
def J1GridGenerator() :
    Grille2Mots = []
    i = 0
    while i < 2:
        Grille2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(Grille2Mots)
J1GridGenerator()

print("Grille Joueur 2 :")
def J2GridGenerator() :
    Grille2Mots = []
    i = 0
    while i < 2:
        Grille2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(Grille2Mots)
J2GridGenerator()

truc = input("Joueur 1 souhaitez-vous rafraîchir votre liste ?")

if truc == "Oui" or truc == "oui":
    print("Nouvelle liste Joueur 1 :")
    J1GridGenerator()

truc2 = input("Joueur 2 souhaitez-vous rafraîchir votre liste ?")

if truc2 == "Oui" or truc2 == "oui":
    print("Nouvelle liste Joueur 2 :")
    J2GridGenerator()

# Choix de mot
# input("Votre mère")
# print("La phrase du joueur 1 est composée de" PhraseJ1 )

# OptionFinir
# OptionResetListePerso = Tasse de thé
# Si le joueur sélectionne Option Finir qu'il aura parmi ses choix de mots