from hytte import Hytte
class Tur:
    def __init__(self,listeMedHytter,beskrivelse):
        self._listeMedHytter = listeMedHytter
        self._turBeskrivelse = beskrivelse


    def skrivTur(self):
        print("Tur beskrivelse: " + self._turBeskrivelse)
        print()
        for hytte in self._listeMedHytter:
            hytte.skrivHytte()

    def sjekkPrisPlass(self,antall_person,maksbelop):
        for hytte in self._listeMedHytter:
            hyttePris = hytte.totPris(antall_person)
            harPlass = hytte.sjekkPlass(antall_person)
            if (hyttePris < maksbelop) and (harPlass == True):
                return True
        return False

    def hentHytte(self):
        return self._listeMedHytter
