#Oppgave 3a
def hastighet(fart):
    if fart <= 60:
        return "fart: " + str(fart)
    else:
        return "fart: over 60."
#Oppgave 3b
def sjekkVerdier(tallene,min,max):
    for tall in tallene:
        if tall >= max or tall <= min:
            return False
    return True
#Oppgave 3 c
def hovedprogram():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.settInnHoyre(b)
    a.settInnVenstre(c)
