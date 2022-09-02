def trimZeros(a):
    liste = a
    indeks1 = 0
    indeks2 = -1
    while liste[indeks1] == 0: #Ferdig med aa fjerne 0 foran
        liste.pop(indeks1)
        print(liste)

    while liste[indeks2] == 0:
        liste.pop(indeks2)

    return liste
