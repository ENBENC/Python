from ukedag import Ukedag
from ukeplan import Ukeplan
from familie import Familie
mandag = Ukedag("mandag")
tirsdag = Ukedag("tirsdag")
mandag1 = Ukedag("mandag1")

tirsdag.settInn("loping",11)
tirsdag.settInn("lese",12)
tirsdag.settInn("loping",13)
tirsdag.settInn("sove",22)
mandag.settInnLedig("jogge")
mandag.settInnLedig("svomme")
mandag.settInnLedig("forlesning")
tirsdag.settInnLedig("forlesning")
tirsdag.settInnLedig("forlesning")
tirsdag.settInnLedig("forlesning")
mandag.settInnLedig("hei")
mandag1.settInnLedig("120121")

ole = Ukeplan("Ole")
per = Ukeplan("per")
ole.settInnDag(mandag1)
#print(mandag.antall())
#print(tirsdag.antall())
per.settInnDag(mandag)
per.settInnDag(tirsdag)
liste = [per,ole]
familie = Familie(liste)
familie.skrivAktiviteter()
