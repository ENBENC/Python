from attraksjon import Attraksjon
class Destinasjon:
    def __init__(self,DeNavn,samling):
        self._DeNavn = DeNavn
        self._samling = samling #Liste med attraksjon objekt

    def skrivDest(self):
        print("Destinasjon Navn: " + str(self._DeNavn))
        for attraksjon in self._samling:
            attraksjon.skrivAttr()

    def leggTilAttr(self,nyAttr):
        self._samling.append(nyAttr) #nyAttr er et objekt

    def antallAktuelleAttr(self,barn,fraDato,tilDato):
        attraksjon_liste = []
        if barn == True:
            for attraksjon in self._samling:
                if attraksjon.forBarn() == True and attraksjon.aapenIPeriode(fraDato,tilDato) == True:
                    attraksjon_liste.append(attraksjon)
        elif barn == False:
            for attraksjon in self._samling:
                if attraksjon.aapenIPeriode(fraDato,tilDato) == True:
                    attraksjon_liste.append(attraksjon)

        return len(attraksjon_liste)
