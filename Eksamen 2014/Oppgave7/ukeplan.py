from ukedag import Ukedag
class Ukeplan:
    def __init__(self,hvem):
        self._hvem = hvem
        self._dager = [] #en liste med antall dager i uke

    def settInnDag(self,dag):
        self._dager.append(dag)

    def travlest(self):
        travlest_dag = self._dager[0].antall()
        dagen = self._dager[0]
        for dag in self._dager:
            if dag.antall() > travlest_dag:
                travlest_dag = dag.antall()
                dagen = dag
        return dagen

    def skrivUt(self):
        print("Ukeplan for " + self._hvem + ": ")
        for dag in self._dager:
            print(dag) #kan printer objektet direkte fordi objektet har en __str__
            print()

    def hentAlleAktiviteterIUke(self):
        liste_alleAktivitet = []
        for dag in self._dager:
            aktivitet_liste = dag.hentAktivitet()
            for aktivitet_navn in aktivitet_liste:
                liste_alleAktivitet.append(aktivitet_navn)

        return liste_alleAktivitet
