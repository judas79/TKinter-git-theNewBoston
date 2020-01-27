from tkinter import *
from tkinter import ttk

root = Tk()         # creates a blank window named root
root.title('Roddy') # renames title to Roddy

# Two different functions demonstrating two techniques with almost the same outcome:
# In the second technique, it invokes the function once you click down the mouse button, but in the first technique, it invoke the function only when you release the button.
# The behavior of the first technique is the desired one, as it allows you to regret and move the mouse away from the button.

def print_name():
    print('Hello, my name is Robot-')

# this is called, binding a function to a widget

button1 = Button(root, text= 'what is your name?', command= print_name) # command calls a function when the button is pressed.  Notice no parenthasis after print_name
button1.pack()

def print_name2(event): # an event can be, clicking something, scrolling, typing, mouse movement of any kind
    print('Hello, my name is Robot2-')

# this is called, binding a function to a widget another way

button2 = ttk.Button(root, text= 'and, what is your name?') # command calls a function when the button is pressed.  Notice no parenthasis after print_name
button2.bind('<Button-1>', print_name2) # button2.bind('\r', doSomething, an action) to use the automatically enter button # two parameters": 1 what kind of triger(which is a fleft mouse click) and 2 which function to call
button2.pack()

def callback():
    print('Hey!')

button2.invoke()                    # button2 starts in the on position
button2.config(command = callback)
#button2.state(['disabled'])# does not work unless using ttk.Button, sets state of button enabled or disabled
button2.state(['!disabled'])# does not work unless using ttk.Button, reads if button state is enabled or disabled
#button2.instate(['disabled'])#
print(button2.instate(['!disabled']))

logo = PhotoImage(file='/Users/rodman/PycharmProjects/tkinter/back_large.gif')
button2.config(image = logo, compound= LEFT) #orients the picture to the left side of the button disply
smallLogo = logo.subsample(5,5)              # resizes the logo and saves it as smallLogo
button2.config(image = smallLogo)            # displays the button with the small logo


root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.


# something to work on:  def printName:    variable = Label(root, text="something")

#you make a new Label with no text and in the function you defined the new text like that : label1["text"]="my name is .... " #replace label1 by the name of your Label btw

# instead of creating function try lambda (in Two ways)- 1. sub = Button(root, text='Submit', command=lambda: print("Your info has been submitted"))
# 2. sub.bind("<Button-1>", lambda event: print("Your info has been submitted")) # event after lambda in 2. line act as an argument

