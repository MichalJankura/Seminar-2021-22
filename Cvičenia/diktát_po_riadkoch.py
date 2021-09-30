subor = open("diktat.txt","r",encoding="UTF-8")
text = subor.read()

pocet = 0

for riadok in text:
    pocet += 1
    if (pocet ==1):
        print(riadok)
    else:
        pocet = 000
text.close()


"""
with open("diktat.txt","r",encoding="UTF-8") as f:
    pocet = 0
    for riadok in f:
        pocet +=1
        if pocet % 2 == 0:
            print(riadok)
"""
