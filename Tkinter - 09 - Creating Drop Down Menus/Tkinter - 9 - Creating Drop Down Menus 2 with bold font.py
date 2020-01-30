from tkinter import *


def do_nothing():                                 # Notice this function comes before the main window ie root, is built
    print('this does nothing')

root = Tk()  # creates a blank window named root
root.title('Roddy')  # renames title to Roddy



menu1 = Menu(root, font="helvetica 18 bold")             # building object menu from the Menu class inside main window root
root.config(menu=menu1)        # configures the menu object so tkinter recognizes it as a Menu object; parameter menu, is the software object menu1
                               # tkinter knows that this is now a menu and needs to go at the top, what items to accept ect. and prepars it to add ore items to be built upon it

# Remove the dashed line (- - - - - - - -) above the dropdown list subMenu = Menu(menu, tearoff=0)
# also, to remove that first option that brings the cascade menu to another window: subMenu = Menu(menu, tearoff=0) <--- this 'tearoff' argument removes the option you want

sub_menu = Menu(menu1, font="helvetica 18 bold")         # sub menu being a menu item uses the Menu class to build sub_menu and is within menu1, this makes a blank menu
menu1.add_cascade(label='File', menu=sub_menu)   # to add drop down item functionalit to the empty menu window, add_cascade add dropdown item/ button, then parameters:
                                                 # a label, and what appears in it, which is the sub menu
sub_menu.add_command(label='New Project...', command=do_nothing) # creates a item, New Project... in the sub menu that points to function do_nothing
sub_menu.add_command(label='New', command=do_nothing)            # creates a item, New in the sub menu that points to function do_nothing
sub_menu.add_separator()                                          # add a seperator to the sub menu to seperate different groups within the File cascade
sub_menu.add_command(label='Exit', command=menu1.quit)

# ******************************************************************** Edit Tab ***********************************************************************************
edit_menu = Menu(menu1)
menu1.add_cascade(label='Edit', menu=edit_menu)                   # Be careful to change the menu='' parameter when copy pasting

edit_menu.add_command(label='Undo Typing', command=do_nothing)

# ******************************************************************** View Tab ***********************************************************************************
view_menu = Menu(menu1)
menu1.add_cascade(label='View', menu=view_menu)                   # Be careful to change the menu='' parameter when copy pasting

view_menu.add_command(label='Quick Definition', command=do_nothing)


root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.