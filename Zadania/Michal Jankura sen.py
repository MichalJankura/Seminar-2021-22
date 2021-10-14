file = open("sen.txt","r",encoding="UTF-8")
parametre = file.readline().split()
subor = file.readlines()
snar = []
for i in subor:

    i = i.strip()
    snar.append(i)

print(snar)

import tkinter
canvas = tkinter.Canvas(width =parametre[0],height = parametre[1])
canvas.pack()


canvas.mainloop()
