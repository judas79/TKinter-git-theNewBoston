'''
from tkinter import *

root = Tk()         # creates a blank window named root
root.title('Roddy')

label1 = Label(root, text='Name', fg='blue')
label2 = Label(root, text='Password', fg ="blue")

entry1 = Entry(root,bg='white')    # Entry is used as a field to store input from a user, text or numbers or symbols, one for the Name, in this case
entry2 = Entry(root, bg='gray')    # Entry is used as a field to store input from a user, text or numbers or symbols, one for the password, in this case

label1.grid(row='0', sticky=E)     # grid makes an assigning point, for rows and for columns; default column = 0: sticky is used to align the text in the label: N,S,E or W ie north, south.... E = to the right
label2.grid(row='1')

entry1.grid(row='0', column='1')
entry_input = entry1.get()         # doesn't work needs a button
print(entry_input)
entry2.grid(row='1', column='1')

check_box = Checkbutton(root, text='keep me logged in')
check_box.grid(columnspan='2')

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.
'''

import sys
from tkinter import *
root = Tk()

def MU():
    mtext = m.get()
textLable = Label(root, text='mtext')
print(textLable)

m = StringVar()
root.geometry("450x450+500+300")
root.title("Lets get it !! ")
first = Label(root, text = "What you put here will be * 7 ")
first.pack()
buttoncheck = Button(root, text = "Check answer", command = MU)
buttoncheck.pack()
Enter_first = Entry(root, textvariable = 'm')
Enter_first.pack(

)

root.mainloop()