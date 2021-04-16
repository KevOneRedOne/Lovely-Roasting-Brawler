import random
from listedemots import *

Liste_10_Mots = []
Liste_2_Mots_J1 = []
Liste_2_Mots_J2 = []

# Fonction qui génère la liste de dix mots partagée entre les deux joueurs
def Generateur_Liste_Principale() :
    i = 0
    while i < 10:
        Liste_10_Mots.append(random.choice(Liste1 + Liste2 + Liste3 + Liste4 + Liste5))
        i += 1
# Fonction qui génère la liste de mots individuelle du joueur 1
def Generateur_Liste_Joueur_1() :
    i = 0
    while i < 2:
        Liste_2_Mots_J1.append(random.choice(Liste1 + Liste2 + Liste3 + Liste4 + Liste5))
        i += 1
# Fonction qui génère la liste de mots individuelle du joueur 2
def Generateur_Liste_Joueur_2() :
    i = 0
    while i < 2:
        Liste_2_Mots_J2.append(random.choice(Liste1 + Liste2 + Liste3 + Liste4 + Liste5))
        i += 1


