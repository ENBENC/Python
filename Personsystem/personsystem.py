class Personsystem:
    def __init__(self):
        self._personListe =[]

    def leggTilPerson(self,person):
        self._personListe.append(person)

    def finnPerson(self,navn):
        for person in self._personListe:
            if person.hentNavn() == navn:
                return True
        return False

    
