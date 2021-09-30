   
def zmen (text, znak):
    for znak in znaky:
        for i in range(len(text)):
            if znak == text[i]:
                text = text[:i] + "_" + text[i+1:]
    return text



diktat = "Bystrý strýko Milan by chcel bývať v prepychovom  príbytku. Bitkári sa bijú aj pre nezmysel. Ich piskot trhá uši . V Banskej Bystrici  býva teta Milena.  Stará mama zbiera byliny. V Bytči predali byt. Minulý rok mi rodičia kúpili nové korčule. Myslel som, že sa za pár minút naučím korčuľovať. To bol veľký omyl."
znaky = "yýiíYIÍÝ"

print(f"všetky písmená:{len(diktat)}")
print()

for pismeno in znaky:
    pocet = 0
    for znak in diktat.lower():
        if pismeno == znak:
            pocet += 1
    if pocet > 0:
        print(f"{pismeno}: {pocet}")
    else:
        print("", end = "")

print(zmen(diktat,znaky))
