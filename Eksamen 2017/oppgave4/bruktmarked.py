from kategori import Kategori
class Bruktmarked:
    def __init__(self):
        self._ordbokKat = {}

    def nyKategori(self,katNavn):
        if katNavn in self._ordbokKat:
            return None
        else:
            ny_kat = Kategori(katNavn)
            self._ordbokKat[katNavn] = ny_kat
            return ny_kat

    def finnKategori(self,katNavn):
        if katNavn not in self._ordbokKat:
            return None
        else:
            for key in self._ordbokKat:
                if key == katNavn:
                    return self._ordbokKat[key]

    def tellLaveBud(self):
        antall = 0
        for key in self._ordbokKat:
            antall += self._ordbokKat[key].hentAntallBudiAnnonse()
        return antall
