class Dag:
    def __init__(self,dato,tall):
        self._dato = str(dato)
        self._tall = float(tall)

    def hentRegneMengde(self):
        return self._tall

    def hentDato(self):
        return self._dato
