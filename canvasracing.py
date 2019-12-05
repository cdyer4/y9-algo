from tkinter import*
from random import randint
def redraw():
    c1.delete("all")
    c1.create_rectangle(0, 800, 600, 100, fill="#3366ff")
    c1.create_rectangle(0, 400, 600, 100, fill="#000099")
    c1.create_rectangle(0, 000, 600, 100, fill="#000000")
    c1.create_oval(herox,heroy,herox + sizehero, heroy + sizehero,fill='#990000')
    c1.create_oval(vilx,vily,vilx + sizevil, vily + sizevil,fill='#3366ff')
    c1.create_text(cwidth / 2,
              110,
              text="You've reached")
    c1.create_text(cwidth / 2,
              120,
              text="space!")

def moveup(event):
    global heroy
    heroy = heroy - heromove
    c1.after(1,redraw)

def movehaut(event):
    global vily
    vily = vily - vilmove
    c1.after(1,redraw)


win = Tk()
win.title( "space race" )
cwidth = 100
cheight = 700

sizehero = 30
heromove = 20

sizevil = 30
vilmove = 20

herox = randint(10,10)
heroy = randint(670,670)


vilx = randint(70,70)
vily = randint(670,670)



c1 = Canvas(win,width=cwidth,height=cheight)
c1.pack()


win.bind('<Up>',moveup)
c1.after(10,redraw)

win.bind('<w>',movehaut)
c1.after(10,redraw)

if heroy, herox >= cheight:
    print("red wins")

if vily, vilx >= cheight:
    print("blue wins")

mainloop()
