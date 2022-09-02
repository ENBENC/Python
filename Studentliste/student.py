class Student:
    def __init__(self,navn,brukernavn,telefonnummer):
        self._navn = navn
        self._brukernavn = brukernavn
        self._telefonnummer = telefonnummer

    def printInfo(self):
        print("Navn: " + self._navn)
        print("Brukernavn: " + self._brukernavn)
        print("Telefonnummer: " + str(self._telefonnummer))
