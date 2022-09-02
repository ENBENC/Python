from bud import Bud
class Annonse:
    def __init__(self,annTekst):
        self._annTekst = annTekst
        self._budListe = []

    def __str__(self):
        for bud in self._budListe:
            print(bud)
        return ""

    def hentTekst(self):
        return self._annTekst

    def giBud(self,hvem,belop):
        self._budListe.append(Bud(hvem,belop))

    def hoyesteBud(self):
        hoyeste = -1
        hoyeste_bud = None
        for bud in self._budListe:
            if bud.hentBudStr() > hoyeste:
                hoyeste = bud.hentBudStr()
                hoyeste_bud = bud
        return hoyeste_bud

    def kraftBud(self,hvem,belop,max):
        belopet = belop
        hoyeste = self.hoyesteBud().hentBudStr()
        if belopet > hoyeste:
            belopet = belop
        else:#belopet <= hoyeste
            if belopet+1 < max:
                belopet += 1
            else:
                belopet = max
        self._budListe.append(Bud(hvem,belopet))
    #Siden man skal lage en bud og append det paa listen, dermed er det best aa bruke variabel.
    #Tilslutt lage budet og append den til listen.

    def hentAntallBud(self):
        return len(self._budListe)
