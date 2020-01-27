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
label1.destroy()

photo3 = PhotoImage(file="back_large.gif").subsample(3,3) # import photo to var logo and resize it to 1/3 its size (x,y)
label1 = Label(root, image=photo3)
label1.pack()
#label1.destroy()

# ************** puts an icon and test on title bar doesn't work ***********

root.iconbitmap(r'/Users/rodman/PycharmProjects/tkinter/Icon.ico')
photo4 = root.iconbitmap(r'/Users/rodman/PycharmProjects/tkinter/Icon.ico')
label1 = Label(root, image=photo4)
label1.pack()
root.title("This sucks")
#You can also add photos to a button:

def HelloFunc():
  print("You clicked a Photo-Button")

# root = Tk()
myPhoto = PhotoImage(file="back_large.gif")
myNewButton = Button(root, image=myPhoto) # adding a logo onto a button
myNewButton.pack()
#root.mainloop()




root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.