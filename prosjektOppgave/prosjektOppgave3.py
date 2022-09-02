from fag import Fag
from student import Student

def hovedprogram():
    student1 = Student("Mohamed")
    student2 = Student("Ali")
    student3 = Student("Ole")

    fag1 = Fag("IN1000")
    fag2 = Fag("MAT1100")
    fag3 = Fag("IN1020")

    #Legger til student inn i fag1
    fag1.leggTilStudent(student1)
    student1.leggTilFag(fag1)
    fag2.leggTilStudent(student2)
    student2.leggTilFag(fag1)
    print()

    #legger til student inn i fag2
    fag2.leggTilStudent(student2)
    student2.leggTilFag(fag2)
    fag2.leggTilStudent(student3)
    student3.leggTilFag(fag2)
    print()

    #Legger til student inn i fag3
    fag3.leggTilStudent(student1)
    student1.leggTilFag(fag3)
    fag3.leggTilStudent(student2)
    student2.leggTilFag(fag3)
    fag3.leggTilStudent(student3)
    student3.leggTilFag(fag3)
    print()

    #student1(Mohamed) har "IN1000","IN1020"
    student1.skrivFagPaaStudent()
    print()
    #student2(Ali) har "IN1000","MAT1100","IN1020"
    student2.skrivFagPaaStudent()
    print()
    #student3(Ole) har "MAT1100","IN1020"
    student3.skrivFagPaaStudent()
    print()

    fag1.skrivStudenterVedFag()
    print(fag1.hentAntallStudenter())
    print()
    fag2.skrivStudenterVedFag()
    print(fag2.hentAntallStudenter())
    print()
    fag3.skrivStudenterVedFag()
    print(fag3.hentAntallStudenter())

hovedprogram()
