from student import Student

def sjekkBruker(navn, ordliste):
    sjekk = False
    for key in ordliste:
        if key == navn:
            print("Fant " + navn + ".")
            ordliste[key].printInfo()
            sjekk = True
    if sjekk == False:
        print(navn + " finne ikke i systemet.")

def hovedprogram():
    ordliste = {}
    ordliste["Haakon"] = Student("Haakon","Haa","123456789")
    ordliste["Mina"] = Student("Mina","Min","987654321")
    ordliste["Ole"] = Student("Ole","Ole","123987654")

    svar = input("Hvilken student vil du soke etter?: ")
    sjekkBruker(svar,ordliste)

    tall = input("Hvor mange student vil du legger inn?: ")
    tall = int(tall)
    indeks = 0
    while indeks < tall:
        navn = input("Skriv navnet til personen?: ")
        brukernavn = input("Skriv brukernavn til personen?: ")
        telefonnummer = input("Skriv telefonnummer til personen?: ")
        ordliste[navn] = Student(navn,brukernavn,telefonnummer)
        indeks += 1

    print()
    for key in ordliste:
        ordliste[key].printInfo()
        print()


hovedprogram()
