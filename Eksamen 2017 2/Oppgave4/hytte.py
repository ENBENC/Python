class Hytte:
    def __init__(self,navn,antall_seng,pris):
        self._navn = navn
        self._antallSenger = antall_seng
        self._pris = pris

    def hentNavn(self):
        return self._navn

    def totPris(self,antall_person):
        totalPris = antall_person * self._pris
        return totalPris

    def skrivHytte(self):
        print("Navn: " + self._navn + " Antall senger: " + str(self._antallSenger) + " Pris per seng: " + str(self._pris))

    def sjekkPlass(self,antall_person):
        if antall_person <= self._antallSenger:
            return True
        else:
            return False
