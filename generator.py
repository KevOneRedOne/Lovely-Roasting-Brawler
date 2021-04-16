import random
from listedemots import *

Liste10Mots = []
J1Liste2Mots = []
J2Liste2Mots = []

def MainListGenerator() :
    i = 0
    while i < 10:
        Liste10Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1

def J1ListGenerator() :
    i = 0
    while i < 2:
        J1Liste2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1

def J2ListGenerator() :
    i = 0
    while i < 2:
        J2Liste2Mots.append(random.choice(List1 + List2 + List3 + List4 + List5))
        i += 1


