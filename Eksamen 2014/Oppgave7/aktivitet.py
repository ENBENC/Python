class Aktivitet:
    def __init__(self,hva,kl):
        self._aktNavn = hva
        self._start = kl #Anta at klokketime starter i 0 til 23

    def hentAktNavn(self):
        return self._aktNavn

    def hentStart(self):
        return self._start
