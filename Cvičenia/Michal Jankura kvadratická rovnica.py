import tkinter
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

def kvadraticka_rovnica():
    a,b,c = 1,-6,4
    v_diskriminant = (b**2) - (4*a*c)
    if v_diskriminant < 0:
        print(f"Diskriminant s hodnotou {v_diskriminant} nie je možné počítať")
    else:
        diskriminant = v_diskriminant**(1/2)
        vysledok1,vysledok2 = (-b-v_diskriminant/(2*a)),(-b+v_diskriminant/(2*a))

        canvas.create_text(250,10,text = "Koreň prvý == "+str(vysledok1) + " Koreň druhý == "+ str(vysledok2),font="Arial 10")
kvadraticka_rovnica()

def graf():
    canvas.create_line(250,20,250,500)
    canvas.create_line(0,250,500,250)
graf()
canvas.mainloop()
