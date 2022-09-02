#Oppgave 3a
def penger(femkroninger,kronestykker):
    kr_femKr = 5 * femkroninger
    kr_enKr = 1 * kronestykker
    antall_kr = kr_femKr + kr_enKr
    return antall_kr

#Oppgave 3b
def barnMedVoksen(alder1,alder2):
    if alder1 >= 18 and alder2 < 18:
        return True
    elif alder1 < 18 and alder2 >= 18:
        return True
    else:
        return False
print(barnMedVoksen(18,5))
print(barnMedVoksen(10,20))
print(barnMedVoksen(20,30))

#Oppgave 3c
#1) return True er innafor for løkken, dermed vil den retunere True dersom den første,
#tallet ikke er negative.
#2) f.eks en liste som ser slik ut [1,-1,-4,-4] Den vil retunere True selvom
#listen inneholder negative tall.
#3)
def allePositive(tallene) :
    for tall in tallene :
        if (tall < 0) :
            return False
    return True
#Oppgave 3d)
def fyllTilTi(tallene):
    lengde_av_liste = len(tallene)
    if lengde_av_liste == 10:
        return tallene
    else:
        add_null = 10 - lengde_av_liste
        indeks = 0
        while indeks < add_null:
            tallene.append(0)
            indeks += 1
        return tallene

assert fyllTilTi([1,2,3]) == [1,2,3,0,0,0,0,0,0,0]
assert fyllTilTi([1,2,3,0,0,0,0,0,0,0]) == [1,2,3,0,0,0,0,0,0,0]
#Oppgave3 e)
class Node :
    def __init__ (self, verdi) :
        self._verdi = verdi
        self._neste = None

    def settInn (self, ny) :
        self._neste = ny

    # ...flere metoder vi ikke trenger..

    def skrivMeg (self) :
        print (self._verdi + "\n")
        if self._neste != None :
            self._neste.skrivMeg()

listeStart = Node("a")
listeStart.settInn(Node("b"))
listeStart.skrivMeg()
print()
#Oppgave3 f)
listeStart = Node("c")
a = Node("a")
listeStart.settInn(a)
b = Node("b")
a.settInn(b)
listeStart.skrivMeg()
