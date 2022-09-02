from gave import Gave
from barn import Barn
class Julekalender:
    def __init__(self,liste_navn,gavefil):
        self._apnere = liste_navn
        self._listeGave = []
        self._kalender = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        self._nesteApner = 0
        self._dag = 0
        self._historikk = {}
        self._lesHistorikk("Historikk.txt")
        self._lesGavefil(gavefil)

    def nyDag(self):
        if self._nesteApner == len(self._apnere):
            self._nesteApner = 0
        gave = self._listeGave[self._dag]
        self._apnere[self._nesteApner].apneGave()
        self._listeGave.remove(gave)

        self._dag += 1
        self._nesteApner += 1

    def gaveOversikt(self):
        for barn in self._apnere:
            barn.skrivBarn()
            print()

    def _lesGavefil(self,filnavn):
        fil = open(filnavn)
        for linje in fil:
            liste = linje.strip().split(",")
            self._listeGave.append(Gave(liste[0],float(liste[1])))

    def _lesHistorikk(self,histfilnavn):
        fil = open(histfilnavn)
        for linje in fil:
            liste = linje.strip().split()
            barnNavn = liste[0]
            gaveNavn = []
            for navn in liste:
                if navn != barnNavn:
                    gaveNavn.append(navn)
            self._historikk[barnNavn] = gaveNavn

    def _skrivHistorikk(self,histfilnavn):
        for key in self._historikk:
            print("Barn: " + key)
            print("Gave barnet har faatt: " + str(self._historikk[key]))

    def avvergetLike(self):
        barn = self._apnere[self._nesteApner]
        gave = self._listeGave[self._dag]
        dagen = self._dag
        barnNavn = barn.hentNavn()
        while gave in self._historikk[barnNavn] and dagen<len(self._kalender):
            dagen += 1
            gave = self._listeGave[dagen]

        if gave not in self._historikk[barnNavn]:
            return True
        else:
            return False
