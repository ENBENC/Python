from bok import Bok
from bokhylle import Bokhylle
class Bibliotek:
    def __init__(self):
        self._bibliotek = []

    def finnBoklBibliotek(self,boknavn,utgivelsesaar):
        for bokhylle in self._bibliotek:
            if bokhylle.finnBok(boknavn,utgivelsesaar) == True:
                return bokhylle.hentBok(boknavn,utgivelsesaar)
        return False


    def leggTilBibliotek(self,bok):
        for bokhylle in self._bibliotek:
            if bokhylle.erDetPlass() == True:
                bokhylle.leggTilBok(bok)
                return True
        return False

    def utvidBibliotek(self,antallBokhylle,plassIbokhylle):
        for indeks in range(antallBokhylle):
            self._bibliotek.append(Bokhylle(plassIbokhylle))

    def printBok(self):
        for bokhylle in self._bibliotek:
            bokhylle.hentBoker()

    def printBokhylle(self):
        indeks = 0
        for bokhylle in self._bibliotek:
            print("Bokhylle nr. " + str(indeks) + str(bokhylle.hentBoksamling()))
            indeks += 1
