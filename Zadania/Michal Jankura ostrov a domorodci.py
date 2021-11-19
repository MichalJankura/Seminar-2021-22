import tkinter,random
canvas = tkinter.Canvas(width=500,height=500,bg="blue")
canvas.pack()

def ostrov(x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="purple")

def domorodec(x,y):
    farba = random.choices(["yellow","red","white"])
    canvas.create_oval(x-10, y-10, x+10, y+10,fill=farba)
    canvas.create_polygon(x,y+10,x-15,y+25,x+10,y+25,x,y+10,fill=farba)

def ryby(x,y):
    farba = random.choices(["yellow","pink","white"])
    canvas.create_oval(x-10, y-10, x+10, y+10,fill=farba)
    canvas.create_polygon(x-10,y,x-15,y-15,x-15,y+25,x-10,y,fill=farba)
def kresli(suradnice):
    x = suradnice.x
    y = suradnice.y
    if (x-250)**2 + (y-500)**2 <= 200**2 :
        domorodec(x,y)
    else:
        ryby(x,y)
ostrov(250,500,200)

canvas.bind('<Button-1>',kresli)

canvas.mainloop()
