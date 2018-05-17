from tkinter import *
tk=Tk()
canvas=Canvas(tk,width =1600,height=802)
canvas.pack()
fondo=PhotoImage(file="fondo.gif")
goku=PhotoImage(file="goku.png")
freezer=PhotoImage(file="freezer.png")
poder1=PhotoImage(file="1.png")
canvas.create_image(0,0,anchor=NW,image=fondo)
canvas.create_image(1000,400,anchor=NW,image=goku)
canvas.create_image(80,350,anchor=NW,image=freezer)
canvas.create_image(70,350,anchor=NW,image=poder1)

def movetriangle(event):
    canvas.move(4,5,0)
canvas.bind_all('<KeyPress-Return>',movetriangle)
tk.mainloop()