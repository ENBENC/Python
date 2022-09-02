from kategori import Kategori
class Meny:
    def __init__(self,liste_kategoriNavn):
        self._menyOrdbok = {}
        self._AlleKatNavn = liste_kategoriNavn
        for navn in self._AllekatNavn:
            filnavn = navn + "txt"
            self._lesKategoriFil(filnavn)

    def hentRedusertMeny(self,sjekk_innholdsstoffer):
        ny_meny = {}
        for key in self._menyOrdbok:
            ny_meny[key] = Kategori(key,self._menyOrdbok[key].hentOkRetter)

        return ny_meny
