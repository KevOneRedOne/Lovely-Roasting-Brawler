from generator import *
from characters import Characters
from listedemots import *
from choixjoueurs import *

print()
print("Bienvenue dans notre jeu => Lovely-Roasting-Brawler !")
print()
print("Il s'agit d'un jeu de combat d'insultes entre deux joueurs ! Les règles ? Très simple.")
print("Vous devez, chacun votre tour, completer une insulte avec une liste de mot aléatoire ! Le but est donc de reussir la meilleure insulte !")
print()
print("Que l'insulte gentille soit avec vous !")
print()


#------------------------------------- Choix du personnage----------------------------------------------------------------------------
personnage_1 = Characters("Bryan")
personnage_2 = Characters("Francis")
personnage_3 = Characters("Jean-Michel")
personnage_4 = Characters("Martha")
personnage_5 = Characters("Agnès")

perso_random = [personnage_1.name, personnage_2.name, personnage_3.name, personnage_4.name, personnage_5.name]

print("Veuillez choisir votre personnage Joueur 1 :")

print(personnage_1.name,',', personnage_1.adjective, "Il n'aime pas que l'on parle de ses parents, et qu'on le traite de gamin !")
print(personnage_2.name,',', personnage_2.adjective, "Il ne supporte pas sa vieillesse...")
print(personnage_3.name,',', personnage_3.adjective, "Il possède un égo surdimensionné !")
print(personnage_4.name,',', personnage_4.adjective, "Elle est réagit au quart de tour !")
print(personnage_5.name,',', personnage_5.adjective, "Elle n'aime qu'on critique son sens de la mode !")
print()


#---Choix du personnage par le Joueur 1, s'il se trompe plus de 5 fois---------------------------------------------------------------------------------------- 
#-----------------------Il obtient un personnage aléatoire---------------------------------------------------------------------------------------------------- 

choice_1 = input("Joueur 1, Entrez le prénom du personnage que vous avez choisi : ")
count_error = 0
Player1 = choice_1

while (choice_1 != "Bryan" and choice_1 != "Martha" and choice_1 != "Francis" and choice_1 != "Jean-Michel" and choice_1 != "Agnès") and count_error < 6 :
    choice_1 = input("Veuillez recommencer s'il vous plait. Entrez uniquement le nom du personnage : ")
    count_error += 1
    if count_error == 2:
        print("Attention, au bout de 5 erreurs vous aurez un personnage aléatoire !")
    elif count_error == 4 :
        print("Dernière chance, sinon vous aurez un personnage aléatoire...")
    elif count_error == 5 : 
        Player1 = random.choice(perso_random)
        print("Joueur 1, par défaut vous êtes :", Player1)
        break

#---Choix du personnage par le Joueur 2 , s'il se trompe plus de 5 fois---------------------------------------------------------------------------------------- 
#-----------------------Il obtient un personnage aléatoire----------------------------------------------------------------------------------------------------

choice_2 = input("Joueur 2, Entrez le prénom du personnage que vous avez choisi : ")
count_error = 0
Player2 = choice_2
while (choice_2 != "Bryan" and choice_2 != "Martha" and choice_2 != "Francis" and choice_2 != "Jean-Michel" and choice_2 != "Agnès") and count_error < 6 :
    choice_2 = input("Veuillez recommencer s'il vous plait. Entrez uniquement le nom du personnage : ")
    count_error += 1
    if count_error == 2:
        print("Attention, au bout de 5 erreurs vous aurez un personnage aléatoire !")
    elif count_error == 4 :
        print("Dernière chance, sinon vous aurez un personnage aléatoire...")
    elif count_error == 5 : 
        Player2 = random.choice(perso_random)
        print("Joueur 2, par défaut vous êtes", Player2)
        break


#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

print("Liste Principale :")
MainListGenerator()
print("Liste Joueur 1 :")
J1ListGenerator()
ChoixJ1()
print("Liste Joueur 2 :")
J2ListGenerator()
ChoixJ2()



# Une fonction qui permette de vérifier la cohérence de la phrase.
# Si le joueur sélectionne Option Finir qu'il aura parmi ses choix de mots, balancer la phrase et les fonctions Score les calculent
# Score des phrases en fonction de leur longueur
# Sélectionner un personnage