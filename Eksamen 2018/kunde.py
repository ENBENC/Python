from kategori import Kategori
from meny import Meny
class Kunde:
    def __init__(tlf,unngaaInnholdsstoff):
        self._tlf = tlf
        self._unngaaInnholdsstoff = ungaaInnholdsstoff

    def velgRetter(self,meny_objekt):
        ny_meny = meny_objekt.hentRedusertMeny(self._unngaaInnholdsstoff)
        liste = []
        for key in ny_meny:
            kategori_objekt = ne_meny[key]
            liste_rett = kategori_objekt.hentRetter()
            print(key)
            for rett in liste_rett:
                print(rett)
            input = input("Velg en rett: ")
            if input != "":
                liste.append(input)

        return liste
