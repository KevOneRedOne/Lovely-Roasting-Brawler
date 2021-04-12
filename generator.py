import random
from listedemots import *
Liste10Mots = []
J1Liste2Mots = []
J2Liste2Mots = []
def MainListGenerator() :
    # Liste10Mots = []
    i = 0
    while i < 10:
        Liste10Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(Liste10Mots)

def J1ListGenerator() :
    # J1Liste2Mots = []
    i = 0
    while i < 2:
        J1Liste2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(J1Liste2Mots)

def J2ListGenerator() :
    # J2Liste2Mots = []
    i = 0
    while i < 2:
        J2Liste2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1
    print(J2Liste2Mots)