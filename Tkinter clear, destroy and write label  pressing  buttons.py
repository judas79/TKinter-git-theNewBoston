# https://stackoverflow.com/questions/48600463/how-to-clear-a-label-using-tkinter-when-pressing-a-button
# by: Nae

try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import Tkinter as tk


def clear_widget_text(widget):
    try:
        widget['text'] = ""
    except:
        print('errors')

def print_widget(widget):
    try:
        widget['text'] = entry.get()
    except:
        print('errors')
    entry.delete(0, 'end')

def destroy_widget(widget):
    widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    label = tk.Label(root, text="This will be cleared.")

    entry = tk.Entry(root)

    button = tk.Button(root, text="Clear", command=lambda: clear_widget_text(label))
    button2 = tk.Button(root, text="Destroy", command=lambda: destroy_widget(label))
    button3 = tk.Button(root, text="post entry", command=lambda: print_widget(label))

    label.pack()
    entry.pack()
    button.pack()
    button2.pack()
    button3.pack()
    root.mainloop()