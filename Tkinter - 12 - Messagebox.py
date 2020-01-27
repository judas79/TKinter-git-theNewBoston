from tkinter import *
import tkinter.messagebox
#import tkinter.messagebox as tkmsg

root = Tk()         # creates a blank window named root
root.title('Roddy') # renames title to Roddy

def windowTitle():
    tkinter.messagebox.showinfo('Window title bar for Alert box','popup message in alert box') # parameters: first window title, second is, the text in message box
                                                                                               # built in ok button to close window
def askQuestion():
    labely = Label(root, text='yes')
    labeln = Label(root, text='no')

    answerYN  = tkinter.messagebox.askquestion('Title window question: yes or no', 'window box yes or no question') # popup box that asks a ye or not question
    if answerYN == 'yes':
        print('the answer was yes = ', answerYN)
        labely.pack(pady=50, padx=50)
    else:
        print('the answer was no = ', answerYN)
        labeln.pack(padx=50, pady=50)

def askcontinue():
    labelyc = Label(root, text='continueing')

    answerYN = tkinter.messagebox.askquestion('Title window question, continue? yes or no', 'Do you wish to continue?')
    if answerYN == 'yes':
        print('the answer was yes = ', answerYN)
        labelyc.pack(pady=50, padx=50)
        windowTitle()
        askQuestion()
        askcontinue()
    else:
        if tkinter.messagebox.askokcancel("Quit", "Are you sure you want to quit?"): # asks weather you want to close the app, or cancel the popup box and continue
            root.destroy()
        else:
            windowTitle()
            askQuestion()
            askcontinue()




windowTitle()
askQuestion()
askcontinue()

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.
