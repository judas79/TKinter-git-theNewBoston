from tkinter import *

print('\nEnter Name, color and background color, you want on your button...\n')
f = Tk()
f1 = Frame(f)
f1.pack(side=LEFT)
name = input("Enter name: ")
color = input("Enter color: ")
bgcolor = input("Back ground Color: ")
ta = Button(f1, text=name, fg=color, bg=bgcolor)
ta.pack()

f.mainloop()