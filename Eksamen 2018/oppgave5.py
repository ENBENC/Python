def godkjenn(alder):
    for familie_liste in alder:
        antall_myndigPerson = 0
        for alder in familie_liste:
            if alder >= 18:
                antall_myndigPerson += 1
        if antall_myndigPerson < 1:
            return False
    return True

print(godkjenn([ [10,2,30], [10,1] ])) #False
assert(godkjenn([ [10,2,30], [10,1] ]) == False)
print(godkjenn([  [10,2,30], [20,1] ]))#True
assert(godkjenn([  [10,2,30], [20,1] ]) == True)
