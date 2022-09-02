class Gave:
    def __init__(self,gavens_navn,pris):
        self._gavensNavn = gavens_navn
        self._pris = float(pris)

    def __str__(self):
        streng = "Gaven: " + str(self._gavensNavn) + "\n"
        streng += "Pris: " + str(self._pris) + "\n"
        return streng

    def hentGaveNavn(self):
        return self._gavensNavn

    def hentPris(self):
        return self._pris
