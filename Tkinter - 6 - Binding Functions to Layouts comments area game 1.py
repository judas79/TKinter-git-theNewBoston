'''
from tkinter import *

root = Tk()         # creates a blank window named root
root.title('Roddy') # renames title to Roddy


def print_name():
    print('Hello, my name is Robot-')

# this is called, binding a function to a widget

button1 = Button(root, text= 'what is your name?', command= print_name) # command calls a function when the button is pressed.  Notice no parenthasis after print_name
button1.pack()

def print_name2(event): # an event can be, clicking something, scrolling, typing, mouse movement of any kind
    print('Hello, my name is Robot2-')

# this is called, binding a function to a widget another way

button2 = Button(root, text= 'and, what is your name?') # command calls a function when the button is pressed.  Notice no parenthasis after print_name
button2.bind('<Button-1>', print_name2) # two parameters": 1 what kind of triger and 2 which function to call
button2.pack()

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.
'''

from tkinter import *
root = Tk()

def printName():
    print ("Hello name is Pace!")

button_1 = Button(root, text="Left click to print name", command=printName)
button_1.pack()

def printName2(event):
    print ("Eureka ! You found it.")

button_2 = Button(root, text="Use middle mouse click to find it." )
button_2.bind("<Button-2>",printName2)
button_2.pack()

def printName3(event):
    print ("Good Job!.Here is an icecream.")

button_3 = Button(root, text="Use right click for a treat." )
button_3.bind("<Button-3>",printName3)
button_3.pack()

root.mainloop()