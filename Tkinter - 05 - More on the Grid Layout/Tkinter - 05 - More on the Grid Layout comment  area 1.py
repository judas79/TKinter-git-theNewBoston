# this was found in the comments section for tkinter - 5 tutorial more on grid layout by theNewBoston
# this doesn't work properly

import sys
from tkinter import *
root = Tk()

def MU():
    mtext = m.get()
    print(mtext)

textLable = Label(root, text='mtext')
print(textLable)

m = StringVar()
root.geometry("450x450+500+300")
root.title("Lets get it !! ")
first = Label(root, text="What you put here will be * 7 ")
first.pack()
buttoncheck = Button(root, text="Check answer", command=MU)
buttoncheck.pack()
Enter_first = Entry(root, textvariable='m')
Enter_first.pack()

root.mainloop()