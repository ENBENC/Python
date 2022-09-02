class Rett:
    def __init__(navn,pris,innholdsstoffer):
        self._navn = navn
        self._pris = pris
        self._innholdsstoffer = innholdsstoffer

    def __str__(self):
        streng = "Navn: " + self._navn + " Pris: " + str(self._pris) + " Innholdsstoffer: " + str(self._innholdsstoffer)
        return streng

    def sjekkInnholdOK(self,sjekk_innholdsstoffer):
        for innholdsstoff in self._innholdsstoffer:
            for sjekk_stoff in sjekk_innholdsstoffer:
                if innholdsstoff == sjekk_stoff:
                    return False
        return True

        
