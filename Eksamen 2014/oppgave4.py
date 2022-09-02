def pris(gratis,alder):
    if gratis == True:
        return 0
    else:
        if alder < 18:
            return 100
        else:
            return 200

print(pris(True,10))
print(pris(False,10))
print(pris(False,50))
