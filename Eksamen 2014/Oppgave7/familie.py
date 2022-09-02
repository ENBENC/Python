from ukeplan import Ukeplan
class Familie:
    def __init__(self,familie_liste):
        self._familie = familie_liste #Liste inneholde ukeplan til hvert enkel person i en familie.
        self._forskjelligeAktivitet = []

    def skrivAktiviteter(self):
        for personlig_ukeplan in self._familie:
            liste_aktivitetTilPerson = personlig_ukeplan.hentAlleAktiviteterIUke()
            print(liste_aktivitetTilPerson)
            for aktivitet_navn in liste_aktivitetTilPerson:
                if not aktivitet_navn in self._forskjelligeAktivitet:
                    self._forskjelligeAktivitet.append(aktivitet_navn)
                

        for aktivitet_navn in self._forskjelligeAktivitet:
            print(aktivitet_navn)
