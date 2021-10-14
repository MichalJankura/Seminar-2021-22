import tkinter,random
canvas = tkinter.Canvas(width="600", height="400")
canvas.pack()

file =  open("mozaika.txt","r",encoding="UTF-8")
subor = file.readlines()
farby = []
for i in subor:
    i = i.strip()
    farby.append(i)
    #print(i)
#print(farby)

def mozaika(sirka_platna, vyska_platna):
    x,y = 0,0
    a = random.randrange(1,51)
    while y < vyska_platna + a:
        while x < sirka_platna + a:
            farba = random.choices(farby)#f"#{random.randrange(256):02x}{random.randrange(256):02x}{random.randrange(256):02x}"

            canvas.create_rectangle(x,y,x+a,y+a, fill=farba,outline= farba)
            x += a
        x=0
        y += a

mozaika(600,400)

canvas.mainloop()
