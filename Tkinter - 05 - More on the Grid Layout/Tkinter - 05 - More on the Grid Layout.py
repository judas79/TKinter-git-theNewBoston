from tkinter import *

def entry_input():

    print(entry1.get(), '\n')
    print(entry2.get(), '\n')
    print(entry3.get(), '\n')
    print('button works')

root = Tk()         # creates a blank window named root
root.title('Roddy')

label1 = Label(root, text='Name', fg='blue')
label2 = Label(root, text='Password', fg="blue")
label3 = Label(root, text='Password', fg="blue")

label1.grid(row='0', sticky=E)     # grid makes an assigning point, for rows and for columns; default column = 0: sticky is used to align the text in the label: N,S,E or W ie north, south.... E = to the right
label2.grid(row='1')
label3.grid(row='2')

entry1 = Entry(root, bg='white')    # Entry is used as a field to store input from a user, text or numbers or symbols, one for the Name, in this case
entry2 = Entry(root, bg='gray')    # Entry is used as a field to store input from a user, text or numbers or symbols, one for the password, in this case
entry3 = Entry(root, show="*")     # prints * instead of text, numbers and symbols in the password entry field.

entry1.grid(row='0', column='1')
entry2.grid(row='1', column='1')
entry3.grid(row='2', column='1')

check_box = Checkbutton(root, text='keep me logged in')
check_box.grid(columnspan='2')

button1 = Button(root, text='entry input', command=entry_input)
button1.grid(row=3, column=3)

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.