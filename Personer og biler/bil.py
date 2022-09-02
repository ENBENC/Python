class Bil:
    def __init__(self,farge,merke):
        self._farge = farge
        self._merke = merke
        self._eier = None

    def eieren(self,navn):
        self._eier = navn

    def hentEieren(self):
        return self._eier
