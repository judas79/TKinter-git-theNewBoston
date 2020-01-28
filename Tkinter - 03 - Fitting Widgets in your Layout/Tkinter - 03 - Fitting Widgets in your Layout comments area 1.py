from tkinter import *

root = Tk()         # creates a blank window named root
'''
label1 = Label(root, text='one', fg='black', bg='white')
label1.pack()

label2 = Label(root, text='two', fg='white', bg='green')
label2.pack(fill=X,)

label3 = Label(root, text='three', fg='red', bg='blue')
label3.pack(side=LEFT, fill=Y)
'''

bottomframe = Frame(root)

bottomframe.pack(side=BOTTOM, fill=X)

label = Label(bottomframe, text="label", bg="red", font="Tahoma 7 bold")
label.pack(side=RIGHT)

'''fill=Y is set to not expand by Tkinter by default. You can let it work as is by doing this:
".pack(fill=Y, expand=True)"'''

#  example of one line of code
one = Label(bottomframe, text="something",  bg="blue").pack(fill=Y, expand=True)

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen
