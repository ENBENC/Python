class Brev:
    def __init__(self,avsender,mottaker):
        self._avsender = avsender
        self._mottaker = mottaker
        self._liste = []

    def skrivLinje(self,tekststreng):
        self._liste.append(tekststreng)

    def lesBrev(self):
        print("Hei " + self._mottaker + "!\n")
        for linje in self._liste:
            print(linje)
        print()
        print("Hilsen fra \n" + self._avsender)
