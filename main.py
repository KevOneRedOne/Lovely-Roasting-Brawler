from generator import *
import os
from characters import Characters
from listedemots import *
# from time import sleep
from score import *

print("Bienvenue dans notre jeu => Lovely-Roasting-Brawler !")
print("Il s'agit d'un jeu de combat d'insultes entre deux joueurs ! Les règles ? Très simple.")
print("Vous devez, chacun votre tour, completer une insulte avec une liste de mot aléatoire ! Le but est donc de reussir la meilleure insulte !")
print("Que l'insulte gentille soit avec vous !")
print()

#------------------------------------- Choix du personnage----------------------------------------------------------------------------
personnage_1 = Characters("Bryan")
personnage_2 = Characters("Francis")
personnage_3 = Characters("Jean-Michel")
personnage_4 = Characters("Martha")
personnage_5 = Characters("Agnès")

perso_random = ["Bryan", "Francis", "Jean-Michel", "Martha", "Agnès"]

print(personnage_1)
print(personnage_2)
print(personnage_3)
print(personnage_4)
print(personnage_5)
print()
#---Choix du personnage, si le joueur se trompe plus de 5 fois------------------------------------------------------------------------------------------------ 
#-----------------------Il obtient un personnage aléatoire---------------------------------------------------------------------------------------------------- 

# dictionnaire python
Players = {}

def newPlayer(PlayerName):
    choice = input(PlayerName + " Entrez le prénom du personnage que vous avez choisi : ")
    count_error = 0

    while count_error <= 5:
        for characterName in perso_random:
            if choice == characterName:
                Players[PlayerName] = Characters(choice)
                return Players
        
        choice = input("Veuillez recommencer s'il vous plait : ")
        count_error += 1
        if count_error == 2:
            print("Attention, au bout de 5 erreurs vous aurez un personnage aléatoire !")
        elif count_error == 4 :
            print("Dernière chance, sinon vous aurez un personnage aléatoire...")
        elif count_error == 5 : 
            Players[PlayerName] = Characters(random.choice(perso_random))
            print(PlayerName, "par défaut vous êtes :", Players.get(PlayerName).name)
            return Players
            
Players = newPlayer("Joueur 1")
# print() le nom du personnage choisi
# os.system('cls')

Players = newPlayer("Joueur 2")

# time.sleep(60) # Met en pause le code pendant 60 secondes (1 minutes)

# os.system('cls')


#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

# Fonction qui retire les mots des listes en fonction des mots choisis.
def Remove_WordChosen():
    AddtoPhrase = input("Veuillez choisir un mot :")
    for mot in Liste10Mots :
        if mot == AddtoPhrase :
            Liste10Mots.remove(mot)
    for mot in J1Liste2Mots:
        if mot == AddtoPhrase:
            J1Liste2Mots.remove(mot)
    for mot in J2Liste2Mots:
        if mot == AddtoPhrase:
            J2Liste2Mots.remove(mot)
    if mot != AddtoPhrase :
        while mot != Liste10Mots or mot != J1Liste2Mots or mot != J2Liste2Mots :
            AddtoPhrase = input("Veuillez entrer un mot contenu dans l'une des deux listes svp :")

# Fonctions qui vont rafraîchir les listes des deux joueurs
def RefreshListJoueur1():
    refresh = input("Souhaitez-vous rafraîchir votre phrase. Oui ou Non ?").lower()
    if refresh == "oui" or refresh == " oui":
        J1Liste2Mots.clear()
        J1ListGenerator()
        print(J1Liste2Mots)

def RefreshListJoueur2():
    refresh = input("Souhaitez-vous rafraîchir votre phrase. Oui ou Non ?").lower()
    if refresh == "oui" or refresh == " oui":
        J2Liste2Mots.clear()
        J2ListGenerator()
        print()
        print(J2Liste2Mots)

Phrase_J1 = []
Phrase_J2 = []
finJ1 = False
finJ2 = False
nombre_de_tour = 1
game = True

def gameEnd():
    if finJ1 and finJ2:
        return False
    else:
        return True

MainListGenerator()
J1ListGenerator()
J2ListGenerator()

while (game):
    print("Tour", nombre_de_tour)
    print()
    for joueur in Players:
        if joueur == "Joueur 1" and not finJ1:
            print("Au", joueur, "de jouer")
            print()
            print("Vous avez le choix entre : ") 
            print(Liste10Mots)
            print()
            print("Votre liste actuelle", J1Liste2Mots)
            print()
            RefreshListJoueur1()
            print()
            print("Votre phrase actuelle", " ".join(Phrase_J1))
            # AddtoPhrase = input("Veuillez choisir un mot :")
            print()
            Remove_WordChosen()
            Phrase_J1.append(AddtoPhrase)
            print("Votre phrase actuelle", " ".join(Phrase_J1))
            print()
            print("Voulez-vous totalement finir votre phrase ? (Oui ou Non)")
            print("Si vous finissez totalement votre phrase vous ne jouerez plus avant la fin de la partie")
            stop = input().lower()
            if stop == "oui" or stop == " oui":
                finJ1 = True
        elif joueur == "Joueur 2" and not finJ2:
            print("Au", joueur, "de jouer")
            print()
            print("Vous avez le choix entre : ") 
            print(Liste10Mots)
            print("Votre liste actuelle", J2Liste2Mots)
            print()
            RefreshListJoueur2()
            print()
            print("Votre phrase actuelle", )
            # AddtoPhrase = input("Veuillez choisir un mot :")
            Remove_WordChosen()
            Phrase_J2.append(AddtoPhrase)
            print()
            print("Votre phrase actuelle", " ".join(Phrase_J2))
            print()
            print("Voulez-vous totalement finir votre phrase ? (Oui ou Non)")
            print("Si vous finissez totalement votre phrase vous ne jouerez plus avant la fin de la partie")
            stop = input().lower()
            if stop == "oui" or stop == " oui":
                finJ2 = True
    nombre_de_tour += 1

    if nombre_de_tour == 11:
        break
    else:
        game = gameEnd()

# Fin du jeu ici
print("jeu fini")

print("La phrase du joueur 1 est ", " ".join(Phrase_J1))
print("La phrase du joueur 2 est", " ".join(Phrase_J2))

score1 = print("Score du joueur 1 :", ScoreTotal(Phrase_J1, Players.get("Joueur 2").faiblesse))
score2 = print("Score du joueur 2 :", ScoreTotal(Phrase_J2, Players.get("Joueur 1").faiblesse))
if score1 > score2:
    print("Joueur 1 a gagné !")
else:
    print("Joueur 2 a gagné !")