from personsystem import Personsystem
from person import Person

def hovedprogram():
    personsystem = Personsystem()
    person1 = Person("Per")
    person2 = Person("Ole")
    person3 = Person("Fredrik")
    person4 = Person("Kar")
    person5 = Person("Ola")
    personsystem.leggTilPerson(person1)
    personsystem.leggTilPerson(person2)
    personsystem.leggTilPerson(person3)
    personsystem.leggTilPerson(person4)
    personsystem.leggTilPerson(person5)
    print(personsystem.finnPerson("Per"))
    print(personsystem.finnPerson("Mina"))

hovedprogram()
