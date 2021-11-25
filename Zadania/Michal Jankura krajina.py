import tkinter, random

canvas = tkinter.Canvas(width = 500, heigh = 400, bg= 'skyblue')
canvas.pack()

def kopceky():
    x0 = random.randint(100,400)
    y = random.randint(150,350)
    suradnice = []
    prevysenie = random.choice((1, 2))
    for x in range(0,510,10):
        if x<x0:
            if prevysenie == 1:
                y -= random.randint(0,5)
            else:
                y += random.randint(0,5)
        else:
            if prevysenie == 1:
                y += random.randint(0,5)
            else:
                y -= random.randint(0,5)
        suradnice.append(x)
        suradnice.append(y)
    farba= f'#00{random.randrange(256):02x}00'
    canvas.create_polygon(500,400,0,400,0,y,suradnice, fill = farba, outline = 'green')

def nova_krajinka(zmena):
    canvas.delete('all')
    for i in range(4,10):
        kopceky()

canvas.bind_all('<space>', nova_krajinka)

canvas.mainloop()
 
