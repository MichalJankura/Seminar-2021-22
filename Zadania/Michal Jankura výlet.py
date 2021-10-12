file = open("studenti.txt","r",encoding="UTF-8")
subor = file.readlines()
chlapci = []
dievcata = []
for i in subor:
    i = i.strip()
    if i[-1] == "a" :
        dievcata.append(i)
    else:
        chlapci.append(i)
print("Počet dievčat je",len(dievcata))
print("Počet chlapcov je",len(chlapci))