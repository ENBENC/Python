from side import Side

class Firkant:
    def __init__(self):
        self._hoyre = None
        self._venstre = None
        self._topp = None
        self._bunn = None


    def leggTilSide(self,side_lengde,side_navn,farge):
        side_navn = side_navn.lower()
        print(side_navn)
        if side_navn == "venstre":
            self._venstre = Side(side_lengde,farge)
        elif side_navn == "hoyre":
            self._hoyre = Side(side_lengde,farge)
        elif side_navn == "topp":
            self._topp = Side(side_lengde,farge)
        else:
            self._bunn = Side(side_lengde,farge)

    def fjernSide(self,side_navn):
        side_navn = side_navn.lower()
        if side_navn == "hoyre":
            self._hoyre = None
        elif side_navn == "venstre":
            self._venstre = None
        elif side_navn == "topp":
            self._topp = None
        elif side_navn == "bunn":
            self._bunn = None

    def hentSidehoyre(self):
        return self._hoyre.hentFarge()

    def erFirkant(self):
        sjekk = True
        liste = [self._hoyre,self._venstre,self._topp,self._bunn]
        for side in liste:
            if side != None:
                sjekk = True
            elif side == None:
                sjekk = None

        if sjekk == True:
            return True
        elif sjekk == False:
            return False

    def sjekkFirkanter(self,liste_med_firkanter):
        sjekk = True
        for firkant in liste_med_firkanter:
            if firkant.erFirkant() == True:
                sjekk = True
            else:
                sjekk = False

        if sjekk == True:
            return True
        elif sjekk == False:
            return False
