from fag import Fag
class Student:
    def __init__(self,navn):
        self._navn = navn
        self._fag = []

    def __str__(self):
        return self._navn

    def leggTilFag(self,fag):
        self._fag.append(fag)

    def hentAntallFag(self):
        antallFag = len(self._fag)
        return antallFag

    def hentStudnetNavn(self):
        return self._navn

    def skrivFagPaaStudent(self):
        print("Student: " + self._navn)
        for fag in self._fag:
            print(fag.hentFagNavn())
