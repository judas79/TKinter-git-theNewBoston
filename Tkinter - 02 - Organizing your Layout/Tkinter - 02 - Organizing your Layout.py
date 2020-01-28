#!/usr/bin/env python
#!/usr/bin/python

from tkinter import *

root = Tk()                     # creates a blank window named root

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)  # since the bottom frame is specified to be, at the bottom the top is at the top

button1 = Button(top_frame, text='button 1', highlightbackground='red', fg='yellow')  # creating a widget button instead of text
button2 = Button(top_frame, text='button 2', bg='blue', fg='green')                   # button placement top_frame is the first parameter, what the text displays, the second, and color, fg=, the third
button3 = Button(top_frame, text='button 3', fg='red')                                # fg foreground bg background
# button4 = Button(bottom_frame, text='button 4', highlightcolor='purple')            # at the bottom frame
button4 = Button(bottom_frame, text="Press!", highlightbackground='blue', fg="green") # still the fg color option does not work

button1.pack(side=LEFT)    # this tells the program what and where to display
button2.pack(side=LEFT)
button3.pack(side=LEFT, fill=BOTH, expand=True)
button4.pack(side=BOTTOM)  # The parameters could be left blank since there are no other objects in the bottom frame

root.mainloop()            # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.

'''bottomFrame = Frame(root).pack(side=BOTTOM) ?
btn1 = Button(bottomFrame, text="okay", fg="red").pack()'''
'''from Tkinter import *

Label(None, text='label', fg='green', bg='black').pack()
Button(None, text='button', fg='green', bg='black').pack()

mainloop()

# **************** With ttk:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# background="..." doesn't work...
ttk.Style().configure('green/black.TLabel', foreground='green', background='black')
ttk.Style().configure('green/black.TButton', foreground='green', background='black')

label = ttk.Label(root, text='I am a ttk.Label with text!', style='green/black.TLabel')
label.pack()

button = ttk.Button(root, text='Click Me!', style='green/black.TButton')
button.pack()

root.mainloop()'''