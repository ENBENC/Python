def Funksjon(liste):
    sjekk = True
    indeks1 = 0
    indeks2 = 1
    while indeks2 < len(liste):
        if liste[indeks1] <= liste[indeks2]:
            sjekk = True
        else:
            return False

        indeks1 += 1
        indeks2 += 2

    return sjekk

print(Funksjon([0,1,2,3]))
print(Funksjon([2,3,2,1]))
print(Funksjon([1,2,7]))
print(Funksjon([1,1,1,1,1]))
