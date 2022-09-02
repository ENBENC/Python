from bruktmarked import Bruktmarked
from kategori import Kategori
from annonse import Annonse
def hovedprogram():
    bruktmarked1 = Bruktmarked()
    sykkellykt = bruktmarked1.nyKategori("sykkellykt")
    annonse1 = sykkellykt.nyAnnonse("New Yorker sykkellykt")
    annonse1.giBud("Peter",0)
    annonse1.giBud("Ann",0)
    annonse1.kraftBud("Mary",40,50)
    print(annonse1)
    print(bruktmarked1.tellLaveBud())
hovedprogram()
