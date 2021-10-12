import random
file = open("studenti.txt","r",encoding="UTF-8")
subor = file.readlines()
chlapci = []
dievcata = []
for i in subor:
    i = i.strip()
    if i[-1] == "a" :
        dievcata.append(i)
        dievcata.sort()
    else:
        chlapci.append(i)
        chlapci.sort()


print(dievcata)
print("Počet dievčat je",len(dievcata))
print(chlapci)
print("Počet chlapcov je",len(chlapci))
print("Zodpovedný za večerný program sú :",random.choice(dievcata),"a",random.choice(chlapci))
