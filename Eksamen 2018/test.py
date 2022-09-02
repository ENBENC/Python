from takeaway import TakeAway
def hovedprogram():
    takeAway1 = TakeAway(["Foretter","Hovedretter","Desserter"],"Kunder.txt")
    tlf = input("Skriv telefonnummer ditt: ")
    while tlf != "":
        takeAway1.betjenKunde(tlf)
        tlf = input("Skriv telefonnummer ditt: ")
    print("Programmet avslutter...")

hovedprogram()
