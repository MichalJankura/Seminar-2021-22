with open("Taxík.txt", "a",encoding = "UTF-8") as file:
    zaciatok = 0
    kilometre = []
    zarobok = []
    while zaciatok ==0:
        vzdialenost = float(input("Zadaj počet prejdených km : "))
        cena0,cena1,cena2,cena3 = 0.50,0.45,0.40,0.35
        if 1.0 <= vzdialenost <= 10.0:
            kilometre.append(vzdialenost)
            zarobok.append(vzdialenost*cena0)
            file.write(str(vzdialenost)+" "+str((vzdialenost*cena0)) +"\n")
            print(f"Cena za {vzdialenost}km je {vzdialenost*cena0}€")
        elif 11.0 <= vzdialenost <= 20.0:
            file.write(str(vzdialenost)+" "+str((vzdialenost*cena1)) +"\n")
            print(f"Cena za {vzdialenost}km je {vzdialenost*cena1}€")
        elif 21.0 <= vzdialenost <= 30.0:
            file.write(str(vzdialenost)+" "+str((vzdialenost*cena2)) +"\n")
            print(f"Cena za {vzdialenost}km je {vzdialenost*cena2}€")
        elif 31.0 <= vzdialenost:
            file.write(str(vzdialenost)+" "+str((vzdialenost*cena3)) +"\n")
            print(f"Cena za {vzdialenost}km je {vzdialenost*cena3}€")
        elif 0 == vzdialenost:
            print(f"")
            zaciatok = 1
    file.close()

