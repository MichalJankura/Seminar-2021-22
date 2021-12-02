import turtle
import random
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.speed(0)
pero.up()

def nuholnik(n, a, farba):
    pero.down()
    pero.fillcolor(farba)
    pero.begin_fill()
    for i in range(n):
        pero.forward(a)
        pero.left(360//n)
    pero.end_fill()
    pero.up()
def domcek(f1, f2, a):
    pero.down()
    pero.fillcolor(f1)
    pero.begin_fill()
    for i in range(4):
        pero.forward(a)
        pero.left(90)
    pero.end_fill()
    pero.left(90)
    pero.forward(a)
# def n_farba():
#     ...
# def ulica(rady, stlpce, a):
#     ...
# def nahodne_mesto(pocet):
#     ...

#ulica(7, 3, 30)
#nahodne_mesto(30)
#nuholnik(5,25,"red")
domcek("red","",25)
#pero.hideturtle()
tabula.mainloop()
