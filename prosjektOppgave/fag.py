class Fag:
    def __init__(self,fagnavn):
        self._fagnavn = fagnavn
        self._studentListe = []

    def leggTilStudent(self,student):
        self._studentListe.append(student)

    def hentAntallStudenter(self):
        antallStudenter = len(self._studentListe)
        return antallStudenter

    def hentFagNavn(self):
        return self._fagnavn

    def skrivStudenterVedFag(self):
        print("Fagnavn: "+ self._fagnavn)
        for student in self._studentListe:
            print(student)
