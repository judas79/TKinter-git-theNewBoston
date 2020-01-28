from tkinter import *
from tkinter import ttk

root = Tk()         # creates a blank window named root
counter = 0
the_label = Label(root, text="Hello, I'm right here!, YES over here, idiot", background='yellow') # first parameter where you want the_label is root, the second is text is equal to "hello"
the_label.pack(fill=BOTH, expand=True)    # where to place the widget text within root; pack it anywhere it fits and display it

the_label2 = ttk.Label(root, text= 'Yo-yo')
the_label2.pack()
the_label2.config(text='junpk') # replaces original text
the_label2.config(text='12r3547y5u86970u8pooyojpji-9o7kihjhfgsfadsscsxccvvbbnbmn,m.,.l,;ll[l[ppuououikyuyutyty')# made long on purpose
the_label2.config(wraplength= 100)# word raps the text after 100 pixiles (about 12 letters or symbols, numbers)
the_label2.config(justify=CENTER)# centers the text, written in all caps
the_label2.config(font=('Courier', 14, 'bold')) # configure font properties name of the font then size of font then type of text, the 3rd configuration being optional


the_label3 =Label(root, text='test left', background='blue' )
the_label3.pack(side=LEFT, fill=Y, anchor='nw', ipadx=10, ipady=10 ) # padding to the interior of label3 making it bigger, stores the label3 index name

def label3():
    print('label 3 = ', the_label3)                                  # prints out the content name of label3
    global counter
    if counter == 0:
        the_label3.pack_forget()
        button1.config(text='- click to make label3 re-appear')
        counter += 1
    else:
        the_label3.pack(side=RIGHT, fill=Y, anchor='nw', ipadx=10, ipady=10)
        button1.config(text='- click to make label3 disappear')
        counter = 0

button1 = ttk.Button(root, text='- click to make label3 disappear -', command=label3)
button1.pack()

the_label4 = Label(root, text='test left', background='red')
the_label4.pack(side=LEFT, padx=10, pady=10)                        # pading to the exterior around the_label5
the_label5 = Label(root, text='test left', background='green')
the_label5.pack(side=LEFT, fill=X, expand=True, anchor='ne')        # expands label5 when resizing the window

for widgets in root.pack_slaves():                                  # returns a list of all the widgets index and allows the program to configue the parameters of all the widgets existing within root
    widgets.pack_configure(fill=BOTH, expand=True, side=RIGHT)      # var widgets pack using configure to set parameters
    print(widgets.pack_info())                                      # the pack_info returns a list in the form of a dictionary containing the property values of all the widgets


# ******************************* labels displaying pictures ******************************

the_label2.config(text='fire', foreground ='red') # shortening the amount of text to none
logo = PhotoImage(file='C:\\Users\\Gina\\PycharmProjects\\TKinter-git-theNewBoston\\Tkinter - 1 - Introduction Label\\back_large.gif')

the_label2.config(image=logo)  # Tk supports PNG PTM AND GIF files
the_label2.config(compound='text')
the_label2.config(compound='center') # parameters are 'center', 'left' 'top'

root.mainloop()     # mainloop keeps the root looping infinitely or until closed, so the window remains visible on the screen.
