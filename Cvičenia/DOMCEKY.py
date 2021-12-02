import turtle
import random
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.speed(0)
pero.up()
x,y = -250,150
pero.setpos(x,y)
pero.down()

def nuholnik(n, a, farba):
    pero.down()
    uhol = (n-2)*180
    uhol = 180-(uhol / n)
    pero.fillcolor(farba)
    pero.begin_fill()
    for i in range(n):
        pero.forward(a)
        pero.left(uhol)
    pero.end_fill()
    pero.up()

def domcek(f1, f2, a):
    nuholnik(4,a,f1)
    pero.left(90)
    pero.forward(a)
    pero.right(90)
    nuholnik(3,a,f2)

def n_farba():
    farby = ["red","green","blue"]
    random.choice(farby)
def ulica(rady, stlpce, a):
    for stlp in range(stlpce):
        for rad in range(rady):
            domcek(n_farba(),n_farba(),50)
            pero.up()
            pero.forward(a+50)
            pero.right(90)
            pero.forward(50)
            pero.left(90)
            pero.down()
        pero.up()
        pero.setpos(x,stlp*(-150))
        pero.down()
# def nahodne_mesto(pocet):


ulica(7, 3, 30)
#nahodne_mesto(30)
# domcek("green","red",50)

tabula.mainloop()
