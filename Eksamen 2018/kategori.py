from rett import Rett
class Kategori:
    def __init__(self,kategorinavn,listeMedRetter):
        self._kategorinavn = kategorinavn
        self._listeMedRetter = listeMedRetter

    def hentOkRetter(self,sjekk_innholdsstoffer):
        OkListe = []
        for rett in self._listeMedRetter:
            if rett.sjekkInnholdOK(sjekk_innholdsstoffer) == True:
                OkListe.append(rett)
        return OkListe

    def hentRetter(self):
        return self._listeMedRetter
