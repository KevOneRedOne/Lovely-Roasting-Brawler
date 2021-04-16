def Coherence(point, phrase):
    # Doit contenir au moins un sujet et un verbe pour que la phrase soit correcte
    return point


def ScoreTotal(phrase, faiblesse):
    point = 0
    for elem in phrase:
        point += 3
        for faib in faiblesse:
            if faib == elem:
                point += 2

    point += Coherence(point, phrase) 

    return point