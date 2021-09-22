n = int(input("Zadaj číslo : "))#vstup
hymna = "Nad Tatrou sa blýska , hromy divo bijú"#retazec
d = len(hymna)#zisti pocet písmen v hymne
print(d)#vypíš

for i in range(0,d,n):
    print(hymna[i:i+n])

###riešenie
def rozsekaj(text,sirka):#požadované parametre sú text teda hymna a pocet písmen po kolkých sa bude zalamovať text
    i = 0 #vytvoríme premennú i z hodnotou 0
    while i <= len(text):#kým bude i menšie alebo rovné dĺžke textu sprav:...
        i += sirka
        text = text[:i] + "\n" + text[i:]#text od zaciatku [:i] (pridaj) + "\n" + text do konca[i:]
        i += 1 
    return(text)#vráť upravený text
