from annonse import Annonse
class Kategori:
    def __init__(self,katNavn):
        self._katNavn = katNavn
        self._annonseListe = []

    def nyAnnonse(self,annTekst):
        ny_annonse = Annonse(annTekst)
        self._annonseListe.append(ny_annonse)
        return ny_annonse

    def hetAnnonse(self):
        return self._annonseListe

    def hentAntallBudiAnnonse(self):
        antall = 0
        for annonse in self._annonseListe:
            antall += annonse.hentAntallBud()
        return antall
