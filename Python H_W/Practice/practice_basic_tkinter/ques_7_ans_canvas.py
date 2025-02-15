from tkinter import *


root = Tk()
root.title( "Open Canvas")  # Title
root.geometry("1080x720")   # Screen Size
root.resizable(False, False)     # You can't resize the UI.

def paint( event ):
	
	
	x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 ) 
	
	
	Colour = "#FF0000"      # red color

	w.create_line( x1, y1, x2, 
				y2, fill = Colour )     # Filling with color

w = Canvas(root, width = 1080, height = 720)        # Canvas can be drawn area.
w.bind( "<B1-Motion>", paint )

l = Label( root, text = "Double Click and Drag to draw." )      # Output: Double Click and Drag to draw.
l.pack()
w.pack()

root.mainloop()