from tkinter import *

root = Tk()         # creates a blank window named root
root.title('Roddy') # renames title to Roddy

class roddys_buttons:

    def __init__(self, master): # __init__ is a special function that gets called automatically without calling it by tyoing __init__;
                                #  this ___init__ has parameters self and master; which, var 'master', is root, which is also the same as main window
        frame = Frame(master)   # creates var frame as a Frame and puts it in the master window, also know as root
        frame.pack()            # place it in there and displays frame

        self.printbutton1 = Button(frame, text='button1', command=self.print_message) # create class button, that displays print, printbutton1, which exists within class _init_s' frame,
                                                                                      # the button has text 'button 1' on it, and clicking it triggers a call to def print_message
        self.printbutton1.pack(side=LEFT)                 # puts button1 aligned left and displays it in master frame

        self.quit = Button(frame, text='quit now', command=frame.quit)        # both work on older macs; command,instead of pointing to a def to call uses tkiinter built in,
                                                                              #  command , quit which breaks the main loop, closing the window
        self.quit.pack(side=LEFT)

        self.quit2 = Button(frame, text='quit now 2', command=master.destroy) # works on newer macs
        self.quit2.pack(side=RIGHT)

    def print_message(self):
        print('working')                                       # prints working in the console area

        Label( text="works here").pack(side=BOTTOM,fill=BOTH)  # prints works here on in the label within the frame of the app

b = roddys_buttons(root)                                       # needed an object to actually see the programs within the class so we pass in root, which is also 'master'

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.