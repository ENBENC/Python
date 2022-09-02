class RaskBil:
    def __init__(self,merke,bilnummer,navn,type,toppHastighet):
        self._merke = merke
        self._bilnummer = bilnummer
        self._navn = navn
        self._type = type
        self._toppHastighet = toppHastighet

    def skrivInfo(self):
        print("Merke: " + self._merke)
        print("Bilnummer: " + str(self._bilnummer))
        print("Navn: " + self._navn)
        print("ToppHastighet: " + str(self._toppHastighet))
        if self._type.lower() == "el":
            print("Bil type: EL-bil")
        elif self._type.lower() == "diesel":
            print("Bil type: Diesel-bil")
        elif self._type.lower() == "bensin":
            print("Bil type: Bensin-bil")
        else:
            print("Du har skrevet en feil bil type.")

    def hentMotortype(self):
        return self._type
