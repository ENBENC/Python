from destinasjon import Destinasjon
from attraksjon import Attraksjon
class Katalog:
    def __init__(self,katalogfil):
        self._katalogfil = katalogfil
        self._destKatalog = {}
        self._lesDestinasjonsfil(self._katalogfil)

    def _lesDestinasjonsfil(self,filnavn):
        if :
            D

    def skrivDestListe(self):
        for key in self._destKatalog:
            print(key)

    def skrivEnDest(self,destNavn):
        for navn in self._destKatalog:
            if destNavn = navn:
                print(navn)
                self._destKatalog[navn].skrivDest() #Anta innholdsverdi inneholde en destiansjon objekt.

    def nyAttr(self,destNavn,attrNavn,bVennlig,apenFra,apenTil):
        if destNavn in self._destKatalog:
            self._destKatalog[destNavn].leggTilAttr(Attraksjon(attrNavn,bVennlig,apenFra,apenTil))

    def nyDestFraFil(self,destNavn,filnavn): #eks destNavn = Oslo
        liste_attraksjoner = []
        liste = []
        fil = open(filnavn)
        indeks = 0
        for linje in fil:
            liste.append(linje.strip())

        indeks_antall = (len(liste)/4)
        indeks0 = 0
        indeks1 = 1
        indeks2 = 2
        indeks3 = 3
        while indeks_antall > 0:
            if liste[indeks1] == "VOKSEN":
                liste_attraksjoner.append(Attraksjon(liste[indeks0],False,int(liste[indeks2]),int(liste[indeks3])))
            elif liste[indeks1] == "BARN":
                liste_attraksjoner.append(Attraksjon(liste[indeks0],True,int(liste[indeks2]),int(liste[indeks3])))
            indeks0 += 4
            indeks1 += 4
            indeks2 += 4
            indeks3 += 4
            indeks_antall -=1
        fil.close()

        if destNavn not in self._destKatalog:
            self._destKatalog[destNavn] = Destinasjon(destNavn,liste_attraksjoner)
        elif destNavn in self._destKatalog:
            for attraksjon in liste_attraksjoner:
                self._destKatalog[destNavn].leggTilAttr(attraksjon)

    def finnBesteDest(self,barn,fra,til):
        flest = 0
        lever = None
        for destNavn in self._destKatalog:
            if self._destKatalog[destNavn].antallAktuelleAttr(barn,fra,til) > flest:
                flest = self._destKatalog[destNavn].antallAktuelleAttr(barn,fra,til)
                lever = destNavn

        return lever
