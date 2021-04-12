import random
from listedemots import List1,List2,List3,List4,List5

print("Liste Principale :")
def MainListGenerator() :
    Liste10Mots = []
    i = 0
    while i < 10:
        Liste10Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(Liste10Mots)
MainListGenerator()

print("Liste Joueur 1 :")
def J1ListGenerator() :
    Liste2Mots = []
    i = 0
    while i < 2:
        Liste2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(Liste2Mots)
J1ListGenerator()

print("Liste Joueur 2 :")
def J2ListGenerator() :
    Liste2Mots = []
    i = 0
    while i < 2:
        Liste2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(Liste2Mots)
J2ListGenerator()

truc = input("Joueur 1 souhaitez-vous rafraîchir votre liste ?")

if truc == "Oui" or truc == "oui":
    print("Nouvelle liste Joueur 1 :")
    J1ListGenerator()

truc2 = input("Joueur 2 souhaitez-vous rafraîchir votre liste ?")

if truc2 == "Oui" or truc2 == "oui":
    print("Nouvelle liste Joueur 2 :")
    J2ListGenerator()


# Choix de mot
# input("Votre mère")
# print("La phrase du joueur 1 est composée de" PhraseJ1 )

# OptionFinir
# OptionResetListePerso = Tasse de thé
# Si le joueur sélectionne Option Finir qu'il aura parmi ses choix de mots
# Alterner les tours entre les joueurs
# Score des phrases en fonction de leur longueur
# Sélectionner un personnage