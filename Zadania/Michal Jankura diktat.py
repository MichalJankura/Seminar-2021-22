import re
"""
1. VYTVORENIE PREMENNEJ TEXT
2. VYTVORENIE PREMENNEJ SLOVA KT. VYTVORÍ ZOZNAM SLOV
3. POCET_SLOV SPOČÍTA SLOVÁ ZO ZOZNAMU
4. i ZMEN PÍSMENA V TEXTE NA MALÉ A SPOČITAJ I A Í
5. y ZMEN PÍSMENA V TEXTE NA MALÉ A SPOČITAJ Y A Ý
6. VYP. NÁROčNOSŤ

"""
text = "Kobyla býva v modernom obydlí. Sestra je veľmi bystrá."

slova = text.split()
pocet_slov = len(slova)
i = text.lower().count("i")+text.lower().count("í")
y = text.lower().count("y")+text.lower().count("ý")
difficulty = (i+y)/pocet_slov*100
###
print("Počet slov : ",pocet_slov ,"[i/í]=",i,"[y/ý]=",y ,"Obtiažnosť : ",int(difficulty),"%")
print(re.sub("[iíIÍyýYÝ]","_",text))
# for pismeno in spoluhlasky:
#     pocet = 0
#     for znak in text:
#         if pismeno == znak:
#             pocet +=1
#     print(f"{pismeno}:{pocet}")
#
