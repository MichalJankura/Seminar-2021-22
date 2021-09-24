import re
zmena = str(input("Zadaj písmeno , pre zmenu všetkých samohlások : "))
text = "sedí mucha na stene a spí "
display = re.sub('[aeiouóíúéý]', zmena, text)
print(display)

###RIEŠENIE PODĽA ZADANIA###
# samohlasky = "aeiouóíúéý"
# riekanka = "sedí mucha na stene sedí a spí"
# print(riekanka)
# def zmena(text,n):
#     for znak in samohlasky:
#         text = text.replace(znak,n)
#     print(text)
# n = input("Vlož samohlásku : ")
# zmena(riekanka,n)

###RIEŠENIE PODĽA ZADANIA###
# def zmena(text,samohlaska):
#     zmena = ""
#     for znak in text:
#         if znak in samohlasky:
#             zmena += samohlaska
#         else:
#             zmena += znak
#     return zmena
#
# samohlasky = "aeiouóíúéý"
# riekanka = "sedí mucha na stene sedí a spí"
# print(riekanka)
