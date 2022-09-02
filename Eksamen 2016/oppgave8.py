def besteHus(t):
    antall_seks = 0
    antall_fem = 0
    for tall in t:
        if tall == 6:
            antall_seks +=1
        elif tall == 5:
            antall_fem += 1

    if antall_seks == 3 and antall_fem == 2:
        return True
    else:
        return False

def hus(t):
    ny_liste = []
    for tall in t:
        if tall not in ny_liste:
            ny_liste.append(tall)
    tall1 = ny_liste[0]
    tall2 = ny_liste[1]
    antall_tall1 = 0
    antall_tall2 = 0

    for tall in t:
        if tall == tall1:
            antall_tall1 +=1
        elif tall == tall2:
            antall_tall2 +=1
    if (antall_tall1 == 3 and antall_tall2 ==2) or (antall_tall1 == 2 and antall_tall2 ==3):
        return True
    else:
        return False

print(hus([1,1,1,2,2]))
print(hus([1,1,2,2,2]))
print(hus([1,3,1,2,2]))
