def komenty():
    #c=(x+y)%26
    """rovnica na sifrovanie vraví ,že "x" je náš text a "y" je posun,(x+y) to celé treba videliť počtom písmen v abecede"""
    #c=(x-y)%26
    """rovnica na desifrovanie vraví ,že "x" je náš text a "y" je posun ,(x-y) to celé treba videliť počtom písmen v abecede"""
    #ord(znak) vráti vnútornú reprezentáciu znaku (kódovanie v pamäti počítača)
    """ord('a') bude 97"""
    #chr(číslo) vráti jednoznakový reťazec, pre ktorý má tento znak danú číselnú reprezentáciu
    """chr(97) bude "a" """
    #pozri tabulku
    """https://i1.wp.com/fb.ru/misc/i/gallery/14479/1824337.jpg"""

def vypis_ASII():
    Abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    Zoznam = []#vytvorime prázdny Zoznam
    zoznam = []#vytvorime prázdny zoznam

    for n in Abeceda:
        #print("[",n,ord(n),"]")#vypis pod seba do riadku
        Zoznam.append(n)#v zozname vyskytne sa písmeno Abecedy
        Zoznam.append(ord(n))#v zoznam vyskytne sa kodovanie pismena
    print(Zoznam)

    for i in abeceda:
        #print("[", i, ord(i), "]")#vypis pod seba do riadku
        zoznam.append(i)#v zozname vyskytne sa písmeno abecedy
        zoznam.append(ord(i))#v zoznam vyskytne sa kodovanie pismena
    print(zoznam)
vypis_ASII()

def sifruj(sprava,kluc):#vytvorenie funkcie,pozadoane_parametre text a kluc
    sifra = "" #vytvorili sme si prázdnu premennu sifra
    for znak in sprava:#cyklus nam prejde spravu
        if znak == " ":#ak sa znak == prazdnemu miestu
            sifra += znak#tak pokracuj
        elif znak.isupper() :#inak ak znak je velke pismeno pomocou isupper() vygooglene
            sifra += chr((ord(znak)+kluc-65)%26+65)#ord vytvorí číslo ku kt. + kluc a odpocitame-65 a %26poctom pismen
        else:#inak
            sifra += chr((ord(znak) + kluc - 97) % 26 + 97)
    return sifra

def vstup():
    text = input("Zadaj správu : ")
    print("Pôvodná správa : ",text)
    kluc  = int(input("Zadaj kľúč : "))
    if kluc >=27:
        print("Nemožno šifrovať")
        kluc = int(input("Zadaj kľúč : "))
    else:
        print("Encrypted : ", sifruj(text, kluc))
vstup()