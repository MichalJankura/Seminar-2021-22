abeceda = 'aáäbcčdďeéfghiíjklĺľmnňoóôpqrŕsštťuúvwxyýzž'
#text = 'Aj v tomto školskom roku naše gymnázium ponúka možnosť vzdelávať sa vo voľnočasovom programe s názvom Akadémia veľkých diel'
text = "Vďaka zobrazovaniu reklamy vám môžeme ponúkať viac obsahu. Reklama je dôležitým zdrojom príjmu, vďaka ktorému môžeme zamestnávať kvalitných novinárov a prinášať vám informácie o Slovensku a o svete každý deň."
for pismeno in abeceda:
    pocet = 0
    for znak in text:
        if pismeno == znak.lower():
            pocet += 1
    print(f"{pismeno}:{pocet}")
