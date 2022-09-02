from person import Person

def lesInnPerson(filNavn):
    fil = open(filNavn)
    informasjon = []
    for linje in fil:
        informasjon.append(linje.strip())
    fil.close()

    return Person(informasjon[0],informasjon[1],informasjon[2],informasjon[3],informasjon[4],informasjon[5])

def lagrePerson(person):
    fil = open("person.txt","w")
    fil.write(person.hentNavn() + "\n")
    fil.write(person.hentAddresse() + "\n")
    fil.write(person.hentPostnrPoststed() + "\n")
    fil.write(person.hentLand() + "\n")
    fil.write(person.hentTelf() + "\n")
    fil.write(person.hentTwitter() + "\n")
    fil.close()

def hovedprogram():
    person1 = lesInnPerson("informasjon.txt")
    person1.skrivUtPerson()
    lagrePerson(person1)

hovedprogram()
