from kunde import Kunde
class TakeAway:
    def __init__(self,liste_katNavn,kundefilNavn):
        self._listeKatNavn = liste_katNavn
        self._menyObjekt = None
        self._ordbokKunde = {}
        self._lesKundefil(kundefilNavn) #Denne bygger opp self._menyObjekt og self._ordbokKunde

    def _lesKundefil(self,filnavn):
        fil = open(filnavn)
        for linje in fil:
            unngaa = []
            en_linje = linje.strip().split()
            tlfnr = en_linje[0]
            for element in en_linje:
                if element != tlfnr:
                    unngaa.append(element)
            self._ordbokKunde[tlfnr] = Kunde(tlfnr,unngaa)
        fil.close()

    def _lagOgLeverMat(self,bestilling):
        for rettNavn in bestilling:
            print(rettNavn)

    def betjenKunde(self,tlf):
        kunde = self._ordbokKunde[tlf]

        liste_retter = kunde.velgRetter(self._menyObjekt) #Liste med navn til retter, valget av kunde
        self._lagOgLeverMat(liste_retter)
