konbinasjon = []
to_lik = 0
to_like_konbinasjon = []
for tall in range(1,7):
    for tall2 in range(1,7):
        for tall3 in range(1,7):
            konbinasjonen = str(tall) + "-"+ str(tall2)+"-"+str(tall3)
            konbinasjon.append(konbinasjonen)
            if tall == tall2 or tall == tall3 or tall2 == tall3:
                to_lik +=1
                to_like_konbinasjon.append(konbinasjonen)

for tall in konbinasjon: #Printer alle ulike konbinasjon
    print(tall)


for tall in to_like_konbinasjon: #Printer alle konbinasjon med to like
    print(tall)

print()
print(to_lik) #print antall to like
print(len(konbinasjon))#print antall ulike konbinasjon
