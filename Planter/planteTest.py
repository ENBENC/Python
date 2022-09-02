from plante import Plante

def hovedprogram():
    plante1 = Plante(0,40)
    plante2 = Plante(0,90)
    plante1.vannPlante(10)
    plante2.vannPlante(10)
    plante1.nyDag()
    plante1.nyDag()
    plante2.nyDag()
    plante2.nyDag()
    print(plante1.levende())
    print(plante1.levende())
    print()
    plante3 = Plante(0,30)
    plante3.vannPlante(30)
    plante3.nyDag()
    print(plante3.levende())

hovedprogram()
