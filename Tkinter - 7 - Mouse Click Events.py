import platform
from tkinter import *

root = Tk()         # creates a blank window named root
root.title('Roddy') # renames title to Roddy

def left_click(event):
    label1 = Label(root, text='Left')
    label1.pack(side=TOP, fill=X)
    print('Left')

def middle_click(event):
    print('Double')

def right_click(event):
    print('Right')

print(platform.system())
if platform.system() == "Darwin":
    print("This stuff will be for Mac!")

frame = Frame(root, width='300', height='250') # frame within root, then width and height dimensions

frame.bind('<Button-1>', left_click)   # binds button1 to run def left_click when clicked in windows and mac
frame.bind('<Double-1>', middle_click) # binds button1 to run def DOUBLE_clicked when clicked in windows
frame.bind('<Button-3>', right_click)  # bind the Variable: button_1 to the function printName. The button that says "Print my name" IS button_1,
                                       # click it, and it will say whatever you put in: print("Whatever you want") down in the console


frame.pack(side=BOTTOM, fill=X) # packs it in the root window, but doesn't make it show up there, without a label


root.mainloop()     # mainloop keeps the root lo
