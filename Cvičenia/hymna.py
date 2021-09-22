n = int(input("Zadaj číslo : "))#vstup
hymna = "Nad Tatrou sa blýska , hromy divo bijú"#retazec
d = len(hymna)#zisti pocet písmen v hymne
print(d)#vypíš

for i in range(0,d,n):
    print(hymna[i:i+n])

###
def rozsekaj(text,sirka):
    i = 0
    while i <= len(text):
        i += sirka
        text = text[:i] + "\n" + text[i:]
        i += 1
    return(text)
