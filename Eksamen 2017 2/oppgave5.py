#Oppgave5 a)
def ring(tall,liste):
    while liste[tall] != -1:
        tall = liste[tall]
    return tall

#Oppgave 5 b)
def gyldig(liste):
    maks_hopp = len(liste)
    for tall in liste:
        hoppet = 0
        if tall != -1:
            while liste[tall] != -1:
                tall = liste[tall]
                hoppet += 1
                if hoppet > maks_hopp:
                    return False
    return True

print(gyldig([1,-1,3,4,2]))
print(gyldig([2,-1,-1,0]))
assert gyldig([2, -1, -1, 0])
assert not gyldig([1,-1, 3,4,2])
assert not gyldig([3, -1, -1, 4, 3])
