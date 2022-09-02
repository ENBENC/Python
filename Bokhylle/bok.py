class Bok:
    def __init__(self,tittel,antallSide,utgivelsesaar):
        self._tittel = tittel
        self._antallSide = antallSide
        self._utgivelsesaar = utgivelsesaar

    def hentTittel(self):
        return self._tittel

    def hentUtgivelsesaar(self):
        return self._utgivelsesaar
