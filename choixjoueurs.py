from listedemots import *
from generator import *

def ChoixJ1():
    PhraseJ1 = []
    print("Souhaitez-vous choisir un mot(tapez 'mot') ou rafraîchir la liste de mots (tapez 'refresh)")
    Choix = input("Que souhaitez-vous faire ? ")
    if Choix == "mot" or "Mot":
        AddToPhrase = input("Choisissez un mot parmi les listes ci-dessus : ")
        PhraseJ1.append(AddToPhrase)
        if AddToPhrase in Liste10Mots:
            Liste10Mots.remove(AddToPhrase)
        if AddToPhrase in Liste2Mots:
            Liste2Mots.remove(AddToPhrase)

    print("La phrase du Joueur 1 contient : ",PhraseJ1)
    if Choix == "refresh" or "Refresh":
        print("Nouvelle liste Joueur 1 :")
    J1ListGenerator()

def ChoixJ2():
    PhraseJ2 = []
    print("Souhaitez-vous choisir un mot(tapez 'mot') ou rafraîchir la liste de mots (tapez 'refresh)")
    Choix = input("Que souhaitez-vous faire ? ")
    if Choix == "mot" or "Mot":
        AddToPhrase = input("Choisissez un mot parmi les listes ci-dessus : ")
        PhraseJ2.append(AddToPhrase)
        if AddToPhrase in Liste10Mots:
            MainListGenerator.Liste10Mots.remove(AddToPhrase)
        if AddToPhrase in Liste2Mots:
            J2ListGenerator.Liste2Mots.remove(AddToPhrase)
    print("La phrase du Joueur 2 contient : ",PhraseJ2)
    if Choix == "refresh" or "Refresh":
        print("Nouvelle liste Joueur 2 :")
    J2ListGenerator()