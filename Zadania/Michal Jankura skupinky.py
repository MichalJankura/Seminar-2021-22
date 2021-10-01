import random
def nazov(n):
    samohlasky = "aeiouy"
    spoluhlasky = "qwrtzpasdfghjklmnbvcx"
    meno = " "
    shl = random.choice(samohlasky)
    meno += shl.upper()
    meno += random.choice(spoluhlasky)*n
    meno += shl
    return meno

def zapis():
    global m,n,zoznam
    zoznam = []
    m = int(input("Zadaj pocet skupín :"))
    n  = int(input("Zadaj n : "))
    for i in range(m):
        subor = open("Michal Jankura.txt","a",encoding="UTF-8")
        subor.write(nazov(n)+"\n")

        file = open("Michal Jankura.txt","r",encoding="UTF-8")
        txt = file.read()
        mena_skupin = txt.split()
        zoznam.append(mena_skupin)
    print("Pocet skupín : ",len(mena_skupin)+1)#pocita od nuly
    print(zoznam)
zapis()


