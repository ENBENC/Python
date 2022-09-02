class Side:
    def __init__(self,side_lengde,farge):
        self._sideLengde = side_lengde
        self._farge = farge

    def hentFarge(self):
        return self._farge

    def hentLengde(self):
        return self._sideLengde
