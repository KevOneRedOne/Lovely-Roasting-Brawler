from generateur import *
import os
from personnages import Personnages
from listedemots import *
from score import *

print("Bienvenue dans notre jeu => Lovely-Roasting-Brawler !")
print("Il s'agit d'un jeu de combat d'insultes entre deux joueurs ! Les règles ? Très simple.")
print("Vous devez, chacun votre tour, completer une insulte avec une liste de mot aléatoire ! Le but est donc de reussir la meilleure insulte !")
print("Que l'insulte gentille soit avec vous !")
print()

#------------------------------------- Choix du personnage----------------------------------------------------------------------------
personnage_1 = Personnages("Bryan")
personnage_2 = Personnages("Francis")
personnage_3 = Personnages("Jean-Michel")
personnage_4 = Personnages("Martha")
personnage_5 = Personnages("Agnès")

perso_aleatoire = ["Bryan", "Francis", "Jean-Michel", "Martha", "Agnès"]

print(personnage_1)
print(personnage_2)
print(personnage_3)
print(personnage_4)
print(personnage_5)
print()

#---------------------Choix du personnage, si le joueur se trompe plus de 5 fois------------------------------------------------------------------------------
#-----------------------Il obtient un personnage aléatoire---------------------------------------------------------------------------------------------------- 

# dictionnaire python
Joueurs = {}

def Nouveau_Joueur(Nom_Joueur):
    choix = input(Nom_Joueur + " Entrez le prénom du personnage que vous avez choisi : ")
    nombre_erreurs = 0

    while nombre_erreurs <= 5:
        for Nom_personnage in perso_aleatoire:
            if choix == Nom_personnage:
                Joueurs[Nom_Joueur] = Personnages(choix)
                return Joueurs
        
        choix = input("Veuillez recommencer s'il vous plait : ")
        nombre_erreurs += 1
        if nombre_erreurs == 2:
            print("Attention, au bout de 5 erreurs vous aurez un personnage aléatoire !")
        elif nombre_erreurs == 4 :
            print("Dernière chance, sinon vous aurez un personnage aléatoire...")
        elif nombre_erreurs == 5 : 
            Joueurs[Nom_Joueur] = Personnages(random.choice(perso_aleatoire))
            print(Nom_Joueur, "par défaut vous êtes :", Joueurs.get(Nom_Joueur).nom)
            return Joueurs
            
Joueurs = Nouveau_Joueur("Joueur 1")

Joueurs = Nouveau_Joueur("Joueur 2")


#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

# Fonction qui retire les mots des listes en fonction des mots choisis.
def Retirer_Mot_Choisit(AddtoPhrase, joueur):
    for elem in Liste_10_Mots:
        if elem == AddtoPhrase:
            Liste_10_Mots.remove(elem)
            if joueur == "Joueur 1":
                Phrase_J1.append(AddtoPhrase)
            else:
                Phrase_J2.append(AddtoPhrase)
            return False
    
    if joueur == "Joueur 1":
        for elem in Liste_2_Mots_J1:
            if elem == AddtoPhrase:
                Liste_2_Mots_J1.remove(elem)
                Phrase_J1.append(AddtoPhrase)
                return False
    else:
        for elem in Liste_2_Mots_J2:
            if elem == AddtoPhrase:
                Liste_2_Mots_J2.remove(elem)
                Phrase_J2.append(AddtoPhrase)
                return False

    return True
    
# Fonctions qui vont Reinitialiser les listes individuelles des deux joueurs
def ReinitialiseListeJoueur1():
    reinitialisateur = input("Souhaitez-vous rafraîchir votre phrase. Oui ou Non ?").lower()
    if reinitialisateur == "oui" or reinitialisateur == " oui":
        Liste_2_Mots_J1.clear()
        Generateur_Liste_Joueur_1()
        print(Liste_2_Mots_J1)

def ReinitialiseListeJoueur2():
    reinitialisateur = input("Souhaitez-vous rafraîchir votre phrase. Oui ou Non ?").lower()
    if reinitialisateur == "oui" or reinitialisateur == " oui":
        Liste_2_Mots_J2.clear()
        Generateur_Liste_Joueur_2()
        print()
        print(Liste_2_Mots_J2)


#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

# Création des variables importantes pour le déroulement du jeu
Phrase_J1 = []
Phrase_J2 = []
finJ1 = False
finJ2 = False
nombre_de_tour = 1
jeu = True

# Regarde si les deux joueurs ont fini de completer leur phrase
def Fin_Jeu():
    if finJ1 and finJ2:
        return False
    else:
        return True

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
# Utilisation des fonctions générateurs pour pouvoir créer les listes et donc démarrer la partie
Generateur_Liste_Principale()
Generateur_Liste_Joueur_1()
Generateur_Liste_Joueur_2()
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------

# Déroulement de la partie dans une boucle while, les deux joueurs jouent a la suite. Une fois un tour terminé les deux joueurs peuvent reprendre un mot jusqu'a la fin du jeu
while (jeu):
    print("Tour", nombre_de_tour)
    print()
    for joueur in Joueurs:
        if joueur == "Joueur 1" and not finJ1:
            print("Au", joueur, "de jouer")
            print()
            print("Vous avez le choix entre : ") 
            print(Liste_10_Mots)
            print()
            print("Votre liste personnelle :",Liste_2_Mots_J1)
            print()
            ReinitialiseListeJoueur1()
            print()
            print("Votre phrase actuelle :", " ".join(Phrase_J1))
            AddtoPhrase = input("Veuillez choisir un mot :")
            print()            
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------ Condition pour verifier si le joueur a bien choisi un mot existant dans les listes de mots.
            nombre_erreurs_liste = 0

            while Retirer_Mot_Choisit(AddtoPhrase, joueur):
                nombre_erreurs_liste += 1
                AddtoPhrase = input("Votre mot n'est pas dans la liste, recommencez :")
                if nombre_erreurs_liste == 2 :
                    print ("Attention, vous ne disposez plus que 1 essaie.")
                elif nombre_erreurs_liste == 3 :
                    print("Pour ce tour, vous n'avez pas selectionné de mots. Tant pis !")
                    break
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------    
            print("Votre phrase actuelle :", " ".join(Phrase_J1))
            print()
            print("Voulez-vous totalement finir votre phrase ? (Oui ou Non)")
            print("Si vous finissez totalement votre phrase vous ne jouerez plus avant la fin de la partie")

            # Condition pour stopper le tour du joueur 1 quand il a complété sa phrase.
            stop = input().lower()
            if stop == "oui" or stop == " oui":
                finJ1 = True

        elif joueur == "Joueur 2" and not finJ2:
            print("Au", joueur, "de jouer")
            print()
            print("Vous avez le choix entre : ") 
            print(Liste_10_Mots)
            print("Votre liste personnelle :",Liste_2_Mots_J2)
            print()
            ReinitialiseListeJoueur2()
            print()
            print("Votre phrase actuelle :"," ".join(Phrase_J2))
            AddtoPhrase = input("Veuillez choisir un mot :")
            print()

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
# Condition pour verifier si le joueur a bien choisi un mot existant dans les listes de mots.
            nombre_erreurs_liste = 0

            while Retirer_Mot_Choisit(AddtoPhrase, joueur):
                nombre_erreurs_liste += 1
                AddtoPhrase = input("Votre mot n'est pas dans la liste, recommencez :")
                if nombre_erreurs_liste == 2 :
                    print ("Attention, vous ne disposez plus que 1 essaie.")
                elif nombre_erreurs_liste == 3 :
                    print("Pour ce tour, vous n'avez pas selectionné de mots. Tant pis !")
                    break
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
            print()
            print("Votre phrase actuelle :", " ".join(Phrase_J2))
            print()
            print("Voulez-vous totalement finir votre phrase ? (Oui ou Non)")
            print("Si vous finissez totalement votre phrase vous ne jouerez plus avant la fin de la partie")
            # Condition pour stopper le tour du joueur 2 quand il a complété sa phrase.
            stop = input().lower()
            if stop == "oui" or stop == " oui":
                finJ2 = True
    nombre_de_tour += 1

    if nombre_de_tour == 11:
        break
    else:
        jeu = Fin_Jeu()

#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Fin du jeu ici-----------------------------------------------------------------------------
print("Fin de la partie !")

print("La phrase du joueur 1 est :", " ".join(Phrase_J1))
print("La phrase du joueur 2 est :", " ".join(Phrase_J2))

score1 = ScoreTotal(Phrase_J1, Joueurs.get("Joueur 2").faiblesse)
score2 = ScoreTotal(Phrase_J2, Joueurs.get("Joueur 1").faiblesse)

print("Score du joueur 1 :", score1)
print("Score du joueur 2 :", score2)
if score1 > score2:
    print("Joueur 1 a gagné !")
elif score1 == score2:
    print("Egalité des deux joueurs")
else:
    print("Joueur 2 a gagné !")