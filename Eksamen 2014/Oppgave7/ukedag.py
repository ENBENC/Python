from aktivitet import Aktivitet
class Ukedag:
    def __init__(self,dag):
        self._dag = dag
        self._kl = [] #En liste som skal inneholde klokketime, dersom det er satt opp en aktivitet til det tidspunktet.
        self._aktivitet = []#Liste med aktivitet for dagen.
        self._ledig = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    def __str__(self):
        tekst = self._dag + ": "
        for aktivitet in self._aktivitet:
            tekst += aktivitet.hentAktNavn() + " Kl: " + str(aktivitet.hentStart()) + "\n"

        return tekst

    def hentAktivitet(self):
        liste_med_navn = []
        for aktivitet in self._aktivitet:
            liste_med_navn.append(aktivitet.hentAktNavn())

        return liste_med_navn

    def settInn(self,hva,kl):
        sjekk = True
        for tidspunktet in self._kl:
            if tidspunktet == kl:
                print("Feil, tidspunktet er opptatt.")
                sjekk = False

        if sjekk == True:
            self._aktivitet.append(Aktivitet(hva,kl))
            self._kl.append(int(kl))
            self._ledig.remove(int(kl))


    def tidligste(self):
        if len(self._kl) > 0:
            forste_tidspunkt = self._kl[0]
            for tidspunktet in self._kl:
                if tidspunktet < forste_tidspunkt:
                    forste_tidspunkt = tidspunktet
            return forste_tidspunkt

        elif len(self._kl) == 0:
            return -1

    def seneste(self):
        if len(self._kl) > 0:
            seneste_tidspunkt = self._kl[0]
            for tidspunktet in self._kl:
                if tidspunktet > seneste_tidspunkt:
                    seneste_tidspunkt = tidspunktet
            return seneste_tidspunkt

        elif len(self._kl) == 0:
            return -1

    def antall(self):
        return len(self._aktivitet)

    def hentDag(self):
        return self._dag


    def settInnLedig(self,hva):
        sjekk = True
        if len(self._ledig) == 0:
            print("Det er ingen ledig time idag.")
            sjekk = False

        if sjekk == True:

            if len(self._aktivitet) == 0:
                self.settInn(hva,12)
            else:
                satt_inn = False
                tideligst_tid = self.tidligste()
                senest_tid = self.seneste()
                for tall in range(tideligst_tid+1,senest_tid):
                    for ledig_tid in self._ledig:
                        if tall == ledig_tid and satt_inn !=True:
                            self.settInn(hva,ledig_tid)
                            satt_inn = True

                if satt_inn == False:
                    if senest_tid+1 in self._ledig:
                        self.settInn(hva,senest_tid+1)
                        satt_inn = True
                    elif tideligst_tid-1 in self._ledig:
                        self.settInn(hva,tideligst_tid-1)
                        satt_inn = False

                if satt_inn == False:
                    print("Det er ingen ledig time idag.")
