from tkinter import *

root = Tk()                                               # creates a blank window named root

label1 = Label(root, text='one', fg='black', bg='white')  # fg and bg colors work correctly with Label()
label1.pack(fill=BOTH, expand=True)                       # BOTH, dynamically increases X and Y of the Label;  fill=

label2 = Label(root, text='two', fg='white', bg='green')
label2.pack(fill=X,)

label3 = Label(root, text='three', fg='red', bg='blue')
label3.pack(side=LEFT, fill=Y)                             # pack side=  'TOP' 'BOTTOM' 'LEFT' 'RIGHT'


root.mainloop()                                            # mainloop keeps the root looping infinitely or until closed,
                                                           # so the window remains visible on the screen.