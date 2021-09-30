import random

def generuj_heslo (pm,pv,pc,pz):
    male = "abcdefghijklmnopqrstuvwxyz"
    velke = male.upper()
    cislo = "0123456789"
    heslo = ""
    for i in range(pm):
        heslo += random.choice(male)
    for i in range(pv):
        heslo += random.choice(velke)
    for i in range(pc):
        heslo += random.choice(cislo)
    for i in range(pz):
        heslo += random.choice("+-*/?.:@&#")
    real_heslo = ""
    while len(heslo) > 0:
        i = random.randrange(len(heslo))
        real_heslo += heslo[i]
        heslo = heslo[:i] + heslo[i+1:]
    return real_heslo


m = int(input("pocet malych:"))
v = int(input("pocet velkych:"))
c = int(input("pocet cisel:"))
z = int(input("pocet znakov:"))
p = int(input("Zadaj pocet hesiel : "))

s2 = open("heslá.txt","a",encoding="UTF-8")#a ako append

for q in range (p):
    print("Heslo je:" ,generuj_heslo(m,v,c,z))
    s2.write(generuj_heslo(m,v,c,z)+"\n")#zapíš do súboru
s2.close()

