from side import Side
from firkant import Firkant

firkant1 = Firkant()
firkant2 = Firkant()
firkant1.leggTilSide(1,"venstre","rod")
firkant1.leggTilSide(1,"hoyre","gul")
firkant1.leggTilSide(1,"bunn","blaa")
firkant1.leggTilSide(1,"Topp","graa")

firkant2.leggTilSide(1,"venstre","blaa")
firkant2.leggTilSide(1,"Topp","svart")
firkant_liste = [firkant1,firkant2]
assert(firkant1.sjekkFirkanter(firkant_liste)==False)
print(firkant1.sjekkFirkanter(firkant_liste))
firkant2.leggTilSide(1,"hoyre","graa")
firkant2.leggTilSide(1,"Bunn","rod")
assert(firkant2.sjekkFirkanter(firkant_liste)==True)
assert(firkant1.sjekkFirkanter(firkant_liste)==True)
print(firkant2.sjekkFirkanter(firkant_liste))
print(firkant1.sjekkFirkanter(firkant_liste))
print(firkant2.hentSidehoyre())#graa
