from tkinter import*
import os

def redraw():
    c1.delete("all")
    c1.create_rectangle(0, 0, 100, 50, fill="#000000")

win = Tk()
win.title( "arcadev2" )
cwidth = 100
cheight = 50
v = IntVar()

choice = Label(win,text="choose a game:")
choice.pack( side = TOP )

Button1 = Button(win, text='PvP', fi = open("canvasgame.py")).pack( side = LEFT )
Button2 = Button(win, text='Draw', fill="#3366ff", fi = open("candraw.py")).pack( side = LEFT )
Button3 = Button(win, text='SpaceRace', fi = open("canvasracing.py")).pack( side = LEFT )

Button4 = Button(win, text='Quit', command=quit).pack( side = BOTTOM )

c1 = Canvas(win,width=cwidth,height=cheight)
c1.pack()






mainloop()
