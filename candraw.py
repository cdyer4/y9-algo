from tkinter import *

cwidth = 500
cheight = 150

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   c1.create_oval( x1, y1, x2, y2, fill = python_green )

win = Tk()
win.title( "Drawing game" )
c1 = Canvas(win, 
           width=cwidth, 
           height=cheight)
c1.pack(expand = YES, fill = BOTH)
c1.bind( "<B1-Motion>", paint )

message = Label( win, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )

mainloop()
