def telling(streng):
    liste = []
    for bokstav in streng:
        if bokstav not in liste:
            liste.append(bokstav)
    print(liste)
    return len(liste)

v = telling("accag")
print(v)
