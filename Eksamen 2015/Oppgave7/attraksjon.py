class Attraksjon:
    def __init__(self,navn,barn,fra,til):
        self._navn = navn
        self._barn = barn #True or False
        self._fra = fra
        self._til = til

    def skrivAttr(self):
        print("Navn: " + str(self._navn) + "Barn: " + str(self._barn) + " Fra: " + str(self._fra) + " Til " + str(self._til))

    def forBarn(self):
        return self._barn

    def aapenIPeriode(self,fra,til): #30dager
        if fra >= self._fra and til <= self._til:
            return True
        return False
