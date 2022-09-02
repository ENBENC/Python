class Bokhylle:
    def __init__(self,plass):
        self._antallPlass = plass
        self._ledigPlass = plass
        self._boksamling = []

    def hentBoksamling(self):
        return self._boksamling

    def erDetPlass(self):
        if self._ledigPlass > 0:
            return True
        else:
            return False

    def leggTilBok(self,boken):
        if self.erDetPlass() == True:
            self._boksamling.append(boken)
            self._ledigPlass -= 1
            return True
        else:
            return False

    def finnBok(self,tittel,utgivelsesaar):
        for bok in self._boksamling:
            if bok.hentTittel() == tittel and bok.hentUtgivelsesaar() == utgivelsesaar:
                return True
        return False

    def hentBoker(self):
        for bok in self._boksamling:
            print(bok.hentTittel())

    def hentBok(self,tittel,utgivelsesaar):
        for bok in self._boksamling:
            if bok.hentTittel() == tittel and bok.hentUtgivelsesaar() == utgivelsesaar:
                return bok
