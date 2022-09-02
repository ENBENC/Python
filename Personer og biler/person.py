from bil import Bil
class Person:
    def __init__(self,navn):
        self._navn = navn
        self._mineBiler = []
        self._laanteBiler = []
        self._bilenPersonenHar = []

    def faaInnBil(self,bil):
        if bil.hentEieren() == self._navn:
            self._mineBiler.append(bil)
            self._bilenPersonenHar.append(bil)

    def laanerUt(self,bil):
        if bil in self._bilenPersonenHar:
            self._bilenPersonenHar.remove(bil)

    def laanerInn(self,bil):
        self._laanteBiler.append(bil)
        self._bilenPersonenHar.append(bil)

    def faaLeverteBil(self,bil):
        self._bilenPersonenHar.append(bil)

    def levereBil(self,bil):
        self._laanteBiler.remove(bil)
        self._bilenPersonenHar.remove(bil)

    def hentMineBiler(self):
        return print(self._navn + " sine biler: " + str(self._mineBiler))

    def hentLaanteBiler(self):
        return print(self._navn + " sine biler: " + str(self._laanteBiler))

    def hentHarBil(self):
        return print(self._navn + " har biler: " + str(self._bilenPersonenHar))
