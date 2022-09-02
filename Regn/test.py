from dag import Dag

def lesInnFil(filnavn):
    liste_dag =[]
    fil = open(filnavn)
    for linje in fil:
        delene = linje.strip()
        delene = delene.strip("mm")
        delene = delene.split(" - ") #delene = [dato,regnemengde]
        liste_dag.append(Dag(delene[0],delene[1].replace(",",".")))

    return liste_dag

def dagMax(liste):
    MestNedbor = float(0)
    dag_objekt_med_mest_nedbor = None
    for dag in liste:
        if dag.hentRegneMengde() > MestNedbor:
            MestNedbor = dag.hentRegneMengde()
            dag_objekt_med_mest_nedbor = dag

    return dag_objekt_med_mest_nedbor

def tilsammen(liste):
    samlede_mengde_nedbor = float(0)
    for dag in liste:
        samlede_mengde_nedbor += dag.hentRegneMengde()

    return samlede_mengde_nedbor

def finneSammeMaaned(liste,maaned_navn,aar):
    maaned = []
    for dag in liste:
        liste_dag = dag.hentDato().split()
        if liste_dag[1] == maaned_navn and liste_dag[2] == aar:
            maaned.append(dag)

    return maaned

def besteMaaned(liste):
    liste_med_maaned = []
    forrige_maaned = None
    for dag in liste:
        liste_med_dato = dag.hentDato().split()
        while liste_med_dato[1] != forrige_maaned:
            liste_med_maaned.append(finneSammeMaaned(liste,liste_med_dato[1],liste_med_dato[2]))
            forrige_maaned = liste_med_dato[1]

    minst_nedbor_maaned = liste_med_maaned[0][0].hentDato()
    minste_nedbor = tilsammen(liste_med_maaned[0])
    for maaned in liste_med_maaned:
        if tilsammen(maaned) < minste_nedbor:
            minste_nedbor = tilsammen(maaned)
            minst_nedbor_maaned = maaned[0].hentDato()

    dato_minst_nedbor = minst_nedbor_maaned.split()
    beste = dato_minst_nedbor[1]
    return beste




def hovedprogram():
    #Test lesInnFil
    liste_med_alle_dager = lesInnFil("Nedborsmengder.txt")
    print(liste_med_alle_dager[0].hentDato())
    print(liste_med_alle_dager[0].hentRegneMengde())
    print("Test lesInnFil Ok!")
    print()

    #Test dagMax
    mest_nedbor_dag = dagMax(liste_med_alle_dager)
    print(mest_nedbor_dag.hentDato())
    print(mest_nedbor_dag.hentRegneMengde())
    print("Test dagMax Ok!")
    print()

    #Test tilsammen
    antall_nedbor = tilsammen(liste_med_alle_dager)
    print(antall_nedbor)
    print("Test tilasmmen Ok!")
    print()

    #Test finneSammeMaaned
    maaned = "oktober"
    aar = "2017"
    liste_med_sammeMaaned = finneSammeMaaned(liste_med_alle_dager,maaned,aar)
    for dag in liste_med_sammeMaaned:
        print(dag.hentDato())
    print("Test finneSammeMaaned Ok!")
    print()

    #Test besteMaaned
    beste_maaned = besteMaaned(liste_med_alle_dager)
    print("Beste maaned: ",beste_maaned)
    print()
    print("april",tilsammen(finneSammeMaaned(liste_med_alle_dager,"april","2018")))
    print("mars",tilsammen(finneSammeMaaned(liste_med_alle_dager,"mars","2018")))
    print("februar",tilsammen(finneSammeMaaned(liste_med_alle_dager,"februar","2018")))
    print("januar",tilsammen(finneSammeMaaned(liste_med_alle_dager,"januar","2018")))
    print("desember",tilsammen(finneSammeMaaned(liste_med_alle_dager,"desember","2017")))
    print("november",tilsammen(finneSammeMaaned(liste_med_alle_dager,"november","2017")))
    print("oktober",tilsammen(finneSammeMaaned(liste_med_alle_dager,"oktober","2017")))
    print("Test besteMaaned Ok!")




hovedprogram()
