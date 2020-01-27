from tkinter import *

root = Tk()         # creates a blank window named root
root.title('Roddy')

label1 = Label(root, text='Name', fg='blue')
label2 = Label(root, text='Password', fg ="blue")

entry1 = Entry(root,bg='white')    # Entry is used as a field to store input from a user, text or numbers or symbols, one for the Name, in this case
entry2 = Entry(root, bg='gray')    # Entry is used as a field to store input from a user, text or numbers or symbols, one for the password, in this case

label1.grid(row='0')               # grid makes an assigning point, for rows and for columns; default column = 0
label2.grid(row='1')

entry1.grid(row='0', column='1')
entry2.grid(row='1', column='1')


root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.