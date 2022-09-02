from raskbil import RaskBil

def hovedprogram():
    bil1 = RaskBil("Toyota","12345","Bilen","El",130)
    bil2 = RaskBil("BMW","99321","Fin Bil","Bensin",200)
    bil3 = RaskBil("Yamaha","32142","Nice","Diesel",100)
    liste = [bil1,bil2,bil3]
    for bil in liste:
        bil.skrivInfo()
        print()

    print("Skriver ut kun EL-bil:")
    print()
    for bil in liste:
        if bil.hentMotortype().lower() == "el":
            bil.skrivInfo()


hovedprogram()
