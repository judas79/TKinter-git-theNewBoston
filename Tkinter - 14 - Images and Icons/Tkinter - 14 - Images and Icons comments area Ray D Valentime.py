'''
from tkinter import *

root = Tk()         # creates a blank window named root
root.title('Roddy') # renames title to Roddy

photo1 = PhotoImage(file='5v dual plug Screen Shot 2019-02-16 at 5.05.53 PM.png')
label1 = Label(root, image=photo1)
label1.pack()
label1.destroy()

photo2 = PhotoImage(file="/Users/rodman/Pictures/Screen Shot BJ's 2018-12-20 at 7.58.27 PM.png")
label1 = Label(root, image=photo2)
label1.pack()
'''
# ******************* gif ******************
'''
path = ("Crypt.gif")
img =ImageTk.PhotoImage(Image.open(path))
panel = Label(fen1, image = img)
panel.grid(row = 2, column =0)
'''
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

im = Image.open("back_large.gif")
im.save("back_large.gif")
photo = PhotoImage(file="back_large.gif")
label1 = Label(root, image=photo)
label1.pack()
root.mainloop()

'''
Firstly you must ensure than your image size don't exceed desktop resolution. :) ) Then change it a bit (This works for ALL types of image ) :

from tkinter import *
from PIL import ImageTk, Image # PIL need to installed first
root = Tk()
photo = ImageTk.PhotoImage(Image.open("myface.jpg"))
label = Label(root, image=photo)
label.pack()
'''


# ******************* gif ******************

'''
path = ("Crypt.gif")
img =ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.grid(row = 2, column =0)
'''

# root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.

# completely skipped essentials like treeview, progressbar, radiobutton, spinbox, listbox, create text, like interactive tables