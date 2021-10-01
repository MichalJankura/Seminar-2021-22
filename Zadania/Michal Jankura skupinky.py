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
    global m,n,i
    m = int(input("Zadj pocet skupín :"))
    for i in range(m):
        n  = int(input("Zadaj n : "))
        subor = open("Michal Jankura.txt","a",encoding="UTF-8")
        subor.write(nazov(n)+"\n")
zapis()
print(nazov(n))

