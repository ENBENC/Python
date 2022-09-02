def Funksjon(liste):
    sjekk = True
    forrige_tall = liste[0]

    for tall in liste:
        if tall != forrige_tall:
            sjekk = False

        forrige_tall = tall

    if sjekk == True:
        verdi = int(liste[0])
        return verdi
    elif sjekk == False:
        return -1

print(Funksjon([1,1,1,1]))
print(Funksjon([1,1,2,1,1,1,1]))
print(Funksjon([-1,-1]))

def funksjon(liste):
    sjekk = liste[0]
    for tall in liste:
        if tall != sjekk:
            return -1

    return sjekk

print()
print(funksjon([1,1,1,1]))
print(funksjon([1,1,2,1,1,1,1]))
