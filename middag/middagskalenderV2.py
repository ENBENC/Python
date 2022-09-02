def lesInnMatFil(filnavn):
    filen = open(filnavn)
    matbok = {}
    for linje in filen:
        en_linje = linje.strip().split(", ")
        tid = int(en_linje[1])
        matrett = en_linje[0]
        matbok[matrett] = tid
    filen.close()

    return matbok

def velgMatretter(maks_tid,matbok):
    utvalgAvMat = {}
    for key in matbok:
        if matbok[key] <= maks_tid:
            utvalgAvMat[key] = matbok[key]

    return utvalgAvMat

def skrivMatretterTilFil(matbok):
    fil = open("matrett.txt","w")
    for key in matbok:
        fil.write(key + "," + str(matbok[key])+"\n")
    fil.close()

def hovedprogram():
    tid_maks = input("Maksiaml tid: ")
    if tid_maks.isdigit() == True:
        tid_maks = int(tid_maks)
        matbok = lesInnMatFil("matretter.txt")
        utvalgMatbok = velgMatretter(tid_maks,matbok)
        skrivMatretterTilFil(utvalgMatbok)

    elif tid_maks.isdigit() == False:
        matbok = lesInnMatFil("matretter.txt")
        skrivMatretterTilFil(matbok)

hovedprogram()
