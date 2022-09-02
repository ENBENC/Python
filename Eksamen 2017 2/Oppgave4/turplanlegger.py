from hytte import Hytte
from tur import Tur
class Turplanlegger:
    def __init__(self,filnavnHytte,filnavnTur):
        self._ordbokHytte = {}
        self._listeMedTur = []
        self._hytterFraFil(filnavnHytte)
        self._turerFraFil(filnavnTur)

    def _hytterFraFil(self,filnavn):
        fil = open(filnavn)
        for linje in fil:
            en_linje = linje.strip().split()
            hytteNavn = en_linje[0]
            hytteAntSenger = int(en_linje[1])
            hyttePris = float(en_linje[2])
            self._ordbokHytte[hytteNavn] = Hytte(hytteNavn,hytteAntSenger,hyttePris)
        fil.close()

    def _turerFraFil(self,turfil):
        fil = open(turfil)
        for linje in fil:
            en_listeMed_Hytter = []
            beskrivelse = linje.strip()
            en_linje = linje.strip().split()
            for key in self._ordbokHytte:
                for ord in en_linje:
                    if ord == key:
                        en_listeMed_Hytter.append(self._ordbokHytte[key])
            self._listeMedTur.append(Tur(en_listeMed_Hytter,beskrivelse))


    def finnTurer(self,antall_person,maksbelop,antall_dager):
        liste_hytteSomOppFyllerKrav = []
        for tur in self._listeMedTur:
            if (tur.sjekkPrisPlass(antall_person,maksbelop) == True) and (len(liste_hytteSomOppFyllerKrav) < antall_dager):
                total = 0
                for hytte in tur.hentHytte():
                    total += hytte.totPris(7)
                if total < maksbelop:
                    liste_hytteSomOppFyllerKrav.append(tur)
                    print(total)
        print("Tur som oppfyller Krav: ")
        for tur in liste_hytteSomOppFyllerKrav:
            tur.skrivTur()
            print("----------------------------------------------------------------")
            #print("Hytte som oppfyller krav: ")
            #liste_hytte = tur.hentHytte()
            #krav_hytte = []
            #for hytte in liste_hytte:
            #    if hytte.totPris(antall_person) <= maksbelop:
            #        krav_hytte.append(hytte)
            #for hytte_krav in krav_hytte:
            #    hytte_krav.skrivHytte()
            #print("----------------------------------------")
