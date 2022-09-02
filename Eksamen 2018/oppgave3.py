def vinnerlag(hjemmelag,bortelag,hjemmemaal,bortemaal):
    if hjemmemaal == bortemaal:
        return "uavgjort"
    elif hjemmemaal > bortemaal:
        return "hjemmelag"
    else:
        return "bortelag"

def forkort_lagliste(lagliste):
    forkortetListe = []
    for navn in lagliste:
        if navn not in forkortetListe:
            forkortetListe.append(navn)

    return forkortetListe

def legg_inn_null_maal(lagliste):
    ordbok = {}
    for navn in lagliste:
        ordbok[navn] = 0
    return ordbok

def ekstraher_lagliste(fn):
    liste = []
    fil = open(fn)
    for linje in fil:
        en_linje = linje.strip().split() #en_linje = [navnH,navnB,MH,MB]
        liste.append(en_linje[0])
        liste.append(en_linje[1])
    fil.close()
    return liste

def regn_poengsum(fn):
    liste_med_lagnavn = ekstraher_lagliste(fn)
    liste_med_lagnavn_forkortet = forkort_lagliste(liste_med_lagnavn)
    ordbok_poeng = legg_inn_null_maal(liste_med_lagnavn_forkortet)

    fil = open(fn)
    for linje in fil:
        en_linje = linje.strip().split() #en_linje = [navnH,navnB,MH,MB]
        navn_hjemmelag = en_linje[0]
        navn_bortelag = en_linje[1]
        poeng_hjemmelag = int(en_linje[2])
        poeng_bortelag = int(en_linje[3])

        vinneren = vinnerlag(navn_hjemmelag,navn_bortelag,poeng_hjemmelag,poeng_bortelag)
        if vinneren == "uavgjort":
            ordbok_poeng[navn_hjemmelag] += 1
            ordbok_poeng[navn_bortelag] += 1
        elif vinneren == "hjemmelag":
            ordbok_poeng[navn_hjemmelag] += 3
        else:
            ordbok_poeng[navn_bortelag] += 3
    fil.close()
    return ordbok_poeng

def gull(lagoversikt):
    vinneLag = None
    poeng = 0
    for key in lagoversikt:
        if lagoversikt[key] > poeng:
            vinneLag = key
            poeng = lagoversikt[key]

    return vinneLag

def finn_gull(fn):
    ordbok = regn_poengsum(fn)
    vinneren = gull(ordbok)
    print(vinneren)

def main():
    finn_gull("lag.txt")
main()
