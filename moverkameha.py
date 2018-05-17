from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=450)
canvas.pack()
my_image1=PhotoImage(file="kamepng1.png")
canvas.create_image(300, 225, anchor=NW, image=my_image1)

def movekame(event):
    if event.keysym=='Up':
        canvas.move(1, 0, -3)
    elif event.keysym=='Down':
        canvas.move(1, 0, 3)
    elif event.keysym=='Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)

canvas.bind_all('<KeyPress-Up>', movekame)
canvas.bind_all('<KeyPress-Down>', movekame)
canvas.bind_all('<KeyPress-Left>', movekame)
canvas.bind_all('<KeyPress-Right>', movekame)
tk.mainloop()
