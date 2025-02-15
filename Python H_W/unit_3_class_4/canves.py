from tkinter import *


root = Tk()


root.title( "Paint App ")


root.geometry("500x350")

def paint( event ):
	
	
	x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 ) 
	
	
	Colour = "#FF0000"

	w.create_line( x1, y1, x2, 
				y2, fill = Colour )

w = Canvas(root, width = 400, height = 250) 
w.bind( "<B1-Motion>", paint )

l = Label( root, text = "Double Click and Drag to draw." )
l.pack()
w.pack()

mainloop()