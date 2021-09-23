import re
zmena = str(input("Zadaj písmeno , pre zmenu všetkých samohlások : "))
text = "sedí mucha na stene a spí "
display = re.sub('[aeiouóíúéý]', zmena, text)
print(display)