subor = open("diktat.txt", "r",encoding="UTF-8")

""" "r" ako read
    "w" ako write vytvorí
    "a" ako append
    encoding = "UTF-8" čítanie mäkčeňov
"""
for diktat in subor:
    #diktat = subor.readline()
    print(diktat)
print(len(diktat))#zisti počet znakov z txtu

subor.close()#zavri subor

s2 = open("novýsubor.txt","w",encoding="UTF-8")
s2.write("Aloha")#zapíš do súboru
s2.close()
