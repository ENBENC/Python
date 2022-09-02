class Person:
    def __init__(self,navn,adresse,postnr_poststed,land,telf,twitter):
        self._navn = navn
        self._adresse = adresse
        self._postnr_poststed = postnr_poststed
        self._land = land
        self._telf = telf
        self._twitter = twitter

    def skrivUtPerson(self):
        print("Navn: " + self._navn)
        print("Adresse: " + self._adresse)
        print("Postnr. og poststed: " + self._postnr_poststed)
        print("Land: " + self._land)
        print("Tlfnummer: " + str(self._telf))
        print("Twitter-brukernavn: " + self._twitter)

    def endreNavn(self,endreNavnet):
        self._navn = endreNavnet

    def endreAddresse(self,EndreAddressen):
        self._adresse = EndreAddressen

    def hentNavn(self):
        return self._navn

    def hentAddresse(self):
        return self._adresse

    def hentPostnrPoststed(self):
        return self._postnr_poststed

    def hentLand(self):
        return self._land

    def hentTelf(self):
        return self._telf

    def hentTwitter(self):
        return self._twitter
