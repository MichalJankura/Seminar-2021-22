text = "lastovička"
print(len(text))
print("sto" in text)
print(text[2])
print(text[5:])#od 5písmeno po koniec
print(text[::2])#skáče od začiatkuz po 21
print(text[::-1])#od zadu celé slovo

t1 = text[:2] + "STO" + text[5:]#rozdelenie slova
print(t1)

