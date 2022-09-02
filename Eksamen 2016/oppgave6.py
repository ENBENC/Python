def lesfil(filnavn):
    total = 0
    for linje in open(filnavn):
        utgift = int(linje)
        total += utgift
    return total
print("Peter har brukt: ", lesfil("Peter.txt"))
print("Paul har brukt: ", lesfil("Paul.txt"))
