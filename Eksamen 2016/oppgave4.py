def median(a,b,c):
    liste = [a,b,c]
    minst = a
    storst = a
    for tall in liste:
        if tall < minst:
            minst = tall
    for tall in liste:
        if tall > storst:
            storst = tall
    liste.remove(storst)
    liste.remove(minst)
    return liste[0]

def median2(a,b,c):
    if (a<b and a>c) or (a>b and a<c):
        return a
    elif (b<a and b>c) or (b>a and b<c):
        return b
    elif (c<a and c>b) or (c>a and c<b):
        return b

print(median(3,5,9))
print(median2(3,5,9))
