from turplanlegger import Turplanlegger
from hytte import Hytte
from tur import Tur

def main():
    turplanlegger = Turplanlegger("hytter.txt","turer.txt")
    turplanlegger.finnTurer(7,7000,5)
    #Det er 7 personer og hvert person har 1000kr til aa bruke til overnatting.
    #Det vil si hvert person kan ikke bruke mer enn 200 kr per natt.
    #Til sammen kan ikke 7 personer bruker mer en 1400 kr per natt.
    #Dermed er maksblop per natt 1400kr.
main()
