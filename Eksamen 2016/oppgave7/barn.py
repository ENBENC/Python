from gave import Gave
class Barn:
    def __init__(self,navn):
        self._navn = navn
        self._aapnetGaveListe = []
        self._verdi = 0

    def hentNavn(self):
        return self._navn

    def hentVerdi(self):
        return self._verdi

    def apneGave(self,gave):
        self._aapnetGaveListe.append(gave)
        self._verdi += gave.hentPris()

    def skrivBarn(self):
        print("Barn: " + self._navn)
        print("Gave liste: ")
        for gave in self._aapnetGaveListe:
            print(gave)
            print()
        print("Total verdi: " + str(self._verdi))
        
