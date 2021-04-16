from generator import *
from characters import Characters
from listedemots import *
print()
print("Bienvenue dans notre jeu => Lovely-Roasting-Brawler !\nIl s'agit d'un jeu de combat d'insultes entre deux joueurs ! Les règles ? Très simple.")
print("Vous devez, chacun votre tour, completer une insulte avec une liste de mot aléatoire ! Le but est donc de reussir la meilleure insulte !")
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

# Fonction qui retire les mots des listes les mots choisis.
def Remove_WordChosen():
    for mot in Liste10Mots :
        if mot == AddtoPhrase :
            Liste10Mots.remove(mot)
            print(Liste10Mots)
    for mot in J1Liste2Mots:
        if mot == AddtoPhrase:
            J1Liste2Mots.remove(mot)
            print(J1Liste2Mots)
    for mot in J2Liste2Mots:
        if mot == AddtoPhrase:
            J2Liste2Mots.remove(mot)
            print(J1Liste2Mots)


def RefreshListJoueur1():
    refresh = input("Joueur 1, souhaitez-vous rafraîchir votre phrase. Oui ou Non ?")
    if refresh == "Oui" or refresh == "oui" or refresh == " oui" or refresh == " Oui":
        J1Liste2Mots.clear()
        J1ListGenerator()
        print(J1Liste2Mots)

def RefreshListJoueur2():
    refresh = input("Joueur 2, souhaitez-vous rafraîchir votre phrase. Oui ou Non ?")
    if refresh == "Oui" or refresh == "oui" or refresh == " oui" or refresh == " Oui":
        J2Liste2Mots.clear()
        J2ListGenerator()
        print()
        print(J2Liste2Mots)

Phrase_J1 = []
Phrase_J2 = []
nombre_de_tour = 0
while nombre_de_tour <= 5:
    nombre_de_tour += 1
    print("Tour ", cmpt)
    if nombre_de_tour == 1:
        MainListGenerator()
        J1ListGenerator()
        J2ListGenerator()
    print(Liste10Mots)
    print()
    print("Joueur 1 à votre tour")
    print()
    print("Votre liste actuelle",J1Liste2Mots)
    RefreshListJoueur1()
    print()
    AddtoPhrase = input("Veuillez choisir un mot :")
    print()
    Remove_WordChosen()
    Phrase_J1.append(AddtoPhrase)
    print("Votre phrase actuelle",Phrase_J1)
    print()
    print(Liste10Mots)
    print()
    print("Joueur 2 à votre tour")
    print()
    print("Votre liste actuelle",J2Liste2Mots)
    RefreshListJoueur2()
    print()
    AddtoPhrase = input("Veuillez choisir un mot :")
    Remove_WordChosen()
    Phrase_J2.append(AddtoPhrase)
    print()
    print("Votre phrase actuelle",Phrase_J2)

# Conditions pour éviter que les joueurs rentrent n'importe quoi
# Une fonction qui permette de vérifier la cohérence de la phrase.
# Si le joueur sélectionne Option Finir qu'il aura parmi ses choix de mots, balancer la phrase et les fonctions Score les calculent
# Score des phrases en fonction de leur longueur
