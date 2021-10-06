zoznam = [10,20,30,50,100]
maximum = zoznam[0]
for i in zoznam:
    if maximum < i:
        maximum = i
print("Maximálne číslo zo zoznamu je ",maximum)
"""
1. vytvor zoznam z hodnotami x
2. vytvor premennu maximum a zo zoznamu označ prvé číslo
3. for i in zoznam => prejdi zoznam
4. if i < max ak hodnota i v zozname bude menšia ako maximum,
tak premenna ku maximum = i pridel i a to je max číslo zo zoznamu
"""
"""
Ak chceme nájsť maximum zo zoznamu tak použijeme túto metodu
"""
maximalne_cislo = max(zoznam)
print("MAXIMALNE CISLO JE POMOCOU MAX",maximalne_cislo)