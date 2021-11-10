import random,tkinter
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

d_4 = 0
d_5 = 0
zoznam = []
for i in range(1001):
    cislo = random.randrange(100,999)
    zoznam.append(cislo)

for cislo in zoznam:
    if cislo % 4 == 0:
       d_4 += 1

    if cislo % 5 == 0:
        d_5 += 1
print(f"Delitelné 4 je {d_4} čísel")
print(f"Delitelné 5 je {d_5} čísel")
def graf(a,b):
    canvas.create_line(10,10,10,390)
    canvas.create_line(5,380,300,380)
    canvas.create_rectangle(20,380,40,(380-a),fill="red")
    canvas.create_text(30,390,text="Del 4",font="Arial 10")
    canvas.create_text(30,(380-a-10),text=d_4,font="Arial 10")
    canvas.create_rectangle(60,380,80,(380-b),fill="blue")
    canvas.create_text(70,390,text="Del 5",font="Arial 10")
    canvas.create_text(70,(380-b-10),text=d_5,font="Arial 10")
graf(d_4,d_5)
canvas.mainloop()
