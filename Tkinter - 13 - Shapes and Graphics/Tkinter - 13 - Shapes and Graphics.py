from tkinter import *

root = Tk()         # creates a blank window named root
root.title('Roddy') # renames title to Roddy

canvas1 = Canvas(root, width=200, height=100, bg='gray95')  # create a canvas to draw on
canvas1.pack()

blackLine = canvas1.create_line(0,0,200,100) # default line color is black, then x/y starting point then x/y ending point
redLine = canvas1.create_line(0, 100, 200, 0, fill='red', width=4) # default line color is black, tkinter uses fill to designate color and width for the thickness
greenRectangle = canvas1.create_rectangle(10, 10, 190, 90,outline='brown', width=4) # x/y starting point, then how long x axis line, then y axis length, tkinter uses fill to designate color and width for the thickness
greenSphere = canvas1.create_oval(19, 80, 110, 100, width=6, fill='green') # x/y top left x/y bottom right, tkinter uses fill to designate color and width for the thickness
bluePolygon = canvas1.create_polygon(200, 50, 100, 100, 70, 60, 60, 60, 0, 200, fill='blue') # (x0, y0, x1, y1,...xn, yn, options)

canvas_width = 200
canvas_height = 100
width = canvas_width,
height = canvas_height

points = [0, 0, canvas_width, canvas_height/2, 0, canvas_height]
yellowTriangle = canvas1.create_polygon(points, outline='green',
            fill='yellow', width=3)


x = 0

def delete_greenSphere():
    global x
    if x == 0:
        canvas1.delete(greenSphere)  # makes the greenSphere disapeer
        x = 1
    else:
        canvas1.create_oval(19, 80, 110, 100, width=6, fill='green')   #Draw a new sphere, with same attributes as greenShere, but without a name
        x = 0

Button(root, text='Delete Green Spere', command=delete_greenSphere).pack()

def delete_all():
    canvas1.delete(ALL)         # makes all the canvas items disapeer

Button(root, text='Delete Green Spere', command=delete_all).pack()


root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.