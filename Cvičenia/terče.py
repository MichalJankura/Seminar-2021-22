import turtle
import random
tabula = turtle.Screen()
pero = turtle.Turtle()

def n_farba():
    return f"#{random.randint(100,256**3):06x}"
for j in range(10):
    pozicia = random.randint(0,250)
    pozicia1 = random.randint(0,300)
    for i in range(100,5,-5):
        pero.dot(i,n_farba())
    pero.up()
    pero.setpos(pozicia,pozicia1)
    pero.down()
tabula.mainloop()
