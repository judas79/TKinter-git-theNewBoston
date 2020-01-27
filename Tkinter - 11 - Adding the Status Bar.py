from tkinter import *


def do_nothing():                                 # Notice this function comes before the main window ie root, is built
    print('this does nothing')

root = Tk()  # creates a blank window named root
root.geometry("500x300") 
root.title('Roddy')  # renames title to Roddy

#*************************** Main Menu ***************************************

menu1 = Menu(root)             # building object menu from the Menu class inside main window root
root.config(menu=menu1)        # configures the menu object so tkinter recognizes it as a Menu object; parameter menu, is the software object menu1
                               # tkinter knows that this is now a menu and needs to go at the top, what items to accept ect. and prepars it to add ore items to be built upon it
sub_menu = Menu(menu1)         # sub menu being a menu item uses the Menu class to build sub_menu and is within menu1, this makes a blank menu
menu1.add_cascade(label='File', menu=sub_menu)   # to add drop down item functionalit to the empty menu window, add_cascade add dropdown item/ button, then parameters:
                                                 # a label, and what appears in it, which is the sub menu
sub_menu.add_command(label= 'New Project...', command=do_nothing) # creates a item, New Project... in the sub menu that points to function do_nothing
sub_menu.add_command(label= 'New', command=do_nothing)            # creates a item, New in the sub menu that points to function do_nothing
sub_menu.add_separator()                                          # add a seperator to the sub menu to seperate different groups within the File cascade
sub_menu.add_command(label= 'Exit', command=do_nothing)

edit_menu = Menu(menu1)
menu1.add_cascade(label='Edit', menu=edit_menu)                   # Be careful to change the menu='' parameter when copy pasting

edit_menu.add_command(label='Undo Typing', command=do_nothing)


#******************************** Tool Bar **************************************

toolbar = Frame(root, bg='grey90')                                         # create the toolbar in the Frame and make the background blue

image_button = Button(toolbar, text='Create Image', command=do_nothing)  # create a Button in the toolbar with text create image on it, that points to def do_nothing
image_button.pack(side=LEFT, padx=2, pady=2)                             # Puts the button on the left hand side of the frame and displays it; paddx is padding space on the sides and pady on top and bottom
print_button = Button(toolbar, text='Print Image', command=do_nothing)
print_button.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)                                           # puts the toolbar in the top below the menu window, fills the sides of the buttons, when frame is resized

#******************************** Status Bar **************************************

statusbar = Label(root, text='Prepairing to do nothing...', bd=1, relief=SUNKEN, anchor=W, bg='grey95') # put the statusbar in the main window, root, print text, add a border that equals 1 around the label, how you want the border
                                                                                           #  around the label to appear, is the releif=, and anchor is where the text will be attached, w is west or left the side
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.