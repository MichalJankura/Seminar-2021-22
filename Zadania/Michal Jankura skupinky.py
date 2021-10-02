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
    m = int(input("Zadaj pocet skupín : "))
    n  = int(input("Zadaj n : "))
    for i in range(m):
        subor = open("Michal Jankura.txt", "a", encoding="UTF-8")
        subor.write(nazov(n)+"\n")
        subor.close()
    file = open("Michal Jankura.txt","r",encoding="UTF-8")
    txt = file.read()
    zoznam_skupin = txt.split()

    print("Pocet skupín : ",len(zoznam_skupin))
    print("Zoznam:",zoznam_skupin)
    file.close()
    l = int(input("Pocet skupin na výpis : "))
    for q in range(l):
        print(random.choice(zoznam_skupin))
        subor = open("Michal Jankura.txt", "a", encoding="UTF-8")
        subor.write(random.choice(zoznam_skupin) + "\n")
        subor.close()
        file = open("Michal Jankura.txt", "r", encoding="UTF-8")
        txt = file.read()
        zoznam_skupin = txt.split()
    print("Pocet skupín po generovani: ", len(zoznam_skupin))
zapis()
