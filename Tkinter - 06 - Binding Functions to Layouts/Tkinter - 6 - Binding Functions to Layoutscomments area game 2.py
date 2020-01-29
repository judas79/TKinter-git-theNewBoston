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
button2.bind('<Button-1>', print_name2) # two parameters": 1 what kind of triger and 2 which function to call # button2.bind('\r', doSomething) to use the enter button
button2.pack()

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.

# something to work on:  def printName:    variable = Label(root, text="something")
'''

from tkinter import *

# enter text then display it within the root window.
root = Tk()
text = Label(root, text="Name: ")
text.grid(row=0, column=0, sticky=E)
entry = Entry(root)
entry.grid(row=0, column=1)
entry.focus_set()

def print_name(event):
    name = entry.get()
    label_1 = Label(root, text="Hello " + name)
    label_1.grid(row=2, columnspan=2)
    entry.delete(0, 'end')  # added after theNewBoston lesson to clear the entry (not part of the lesson)

button_1 = Button(root, text = "Press Me", bg = "black", fg = "white")
button_1.bind("<Button-1>", print_name)
button_1.grid(row=1, columnspan=2)

root.mainloop()