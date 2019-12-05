from tkinter import*
from random import randint

def redraw():
    c1.delete("all")
    c1.create_rectangle(0, 0, 800, 600, fill="#009900")
    c1.create_oval(herox,heroy,herox + sizehero, heroy + sizehero,fill='#3366ff')
    c1.create_oval(vilx,vily,vilx + sizevil, vily + sizevil,fill='#ff0000')
    c1.create_oval(treex,treey,treex + sizetree, treey + sizetree,fill='#009940')
    c1.create_oval(tree2x,tree2y,tree2x + sizetree2, tree2y + sizetree2,fill='#009940')
    c1.create_rectangle(rockx,rocky,rockx + sizerock, rocky + sizerock,fill='#4d2600')
    c1.create_rectangle(rock2x,rock2y,rock2x + sizerock2, rock2y + sizerock2,fill='#4d2600')
    c1.create_rectangle(rock3x,rock3y,rock3x + sizerock3, rock3y + sizerock3,fill='#4d2600')

def moveright(event):
    global herox
    herox = herox + heromove
    c1.after(1,redraw)

def moveleft(event):
    global herox
    herox = herox - heromove
    c1.after(1,redraw)

def moveup(event):
    global heroy
    heroy = heroy - heromove
    c1.after(1,redraw)

def movedown(event):
    global heroy
    heroy = heroy + heromove
    c1.after(1,redraw)

def herosword(event):
    global heroy
    if herosword == True():
        c1.create_rectangle(0, 20, 40, 20, fill="#000000")
    c1.after(1,redraw)

def movedoit(event):
    global vilx
    vilx = vilx + vilmove
    c1.after(1,redraw)

def movegauche(event):
    global vilx
    vilx = vilx - vilmove
    c1.after(1,redraw)

def movehaut(event):
    global vily
    vily = vily - vilmove
    c1.after(1,redraw)

def movebas(event):
    global vily
    vily = vily + vilmove
    c1.after(1,redraw)

def vilsword(event):
    global vily
    if vilsword == True():
        c1.create_rectangle(0, 000, 20, 20, fill="#000000")
    c1.after(1,redraw)
    

win = Tk()
win.title( "pvp" )
cwidth = 800
cheight = 600

sizehero = 30
heromove = 20

sizevil = 30
vilmove = 20

sizerock = 50
rockmove = 0

sizerock2 = 50
rock2move = 0

sizerock3 = 50
rock3move = 0

sizetree = 70
treemove = 0

sizetree2 = 70
tree2move = 0

herox = randint(0,cwidth)
heroy = randint(0,cheight)

vilx = randint(0,cwidth)
vily = randint(0,cheight)

rockx = randint(0,cwidth)
rocky = randint(0,cheight)

rock2x = randint(0,cwidth)
rock2y = randint(0,cheight)

rock3x = randint(0,cwidth)
rock3y = randint(0,cheight)

treex = randint(0,cwidth)
treey = randint(0,cheight)

tree2x = randint(0,cwidth)
tree2y = randint(0,cheight)

c1 = Canvas(win,width=cwidth,height=cheight)
c1.pack()

win.bind('<l>',moveright)
c1.after(10,redraw)

win.bind('<j>',moveleft)
c1.after(10,redraw)

win.bind('<i>',moveup)
c1.after(10,redraw)

win.bind('<k>',movedown)
c1.after(10,redraw)

win.bind('<u>',herosword)
c1.after(10,redraw)

win.bind('<d>',movedoit)
c1.after(10,redraw)

win.bind('<a>',movegauche)
c1.after(10,redraw)

win.bind('<w>',movehaut)
c1.after(10,redraw)

win.bind('<s>',movebas)
c1.after(10,redraw)

win.bind('<e>',vilsword)
c1.after(10,redraw)



mainloop()
