def calculation():
    weight = int(input("Zadaj váhu kg : "))
    height = float(input("Zadaj výšku v m (Vzor : 1.8): "))
    bmi = weight//(height**2)
    print(bmi)
    if bmi <= 18.4:
        print("Si chudý.")
    elif bmi <= 24.9:
        print("Si OK :) .")
    elif bmi <= 29.9:
        print("Máš nadváhu.")
    elif bmi <= 34.9:
        print("Máš nadmiernu nadváhu.")
    elif bmi <= 39.9:
        print("Si obézny.")
    else:
        print("Si dosť obézny.")
    return bmi
calculation()
