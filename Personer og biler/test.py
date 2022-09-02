from bil import Bil
from person import Person

def hovedprogram():
    bil1 = Bil("Gul","BMW")
    bil2 = Bil("Rod","Volvo")
    bil3 = Bil("Graa","Toyota")
    bil4 = Bil("Blaa","MinMerke")
    bil5 = Bil("Svart","Volvo")

    person1 = Person("Erik")
    person2 = Person("Alex")
    bil1.eieren("Erik")
    bil2.eieren("Erik")
    bil3.eieren("Alex")
    bil4.eieren("Alex")
    bil5.eieren("Alex")

    person1.faaInnBil(bil1)
    person1.faaInnBil(bil2)
    person2.faaInnBil(bil3)
    person2.faaInnBil(bil4)
    person2.faaInnBil(bil5)
    person1.hentMineBiler()
    person1.hentHarBil()
    person2.hentMineBiler()
    person2.hentHarBil()
    print()

    person1.laanerUt(bil1)
    person2.laanerInn(bil1)
    person1.hentHarBil()
    person2.hentHarBil()
    print()

    person2.levereBil(bil1)
    person1.faaLeverteBil(bil1)
    person1.hentHarBil()
    person2.hentHarBil()


hovedprogram()
