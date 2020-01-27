from tkinter import *

root = Tk()

class FullScreenApp(object):
    def _init_(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

def main():
    menu = Menu(root)

    root.configure(background='white')

    root.config(menu=menu)

# ******************** File Tab **************************

    fileMenu = Menu(menu, tearoff=0) # Gets rid of the '----' in the menu
    menu.add_cascade(label='File', menu=fileMenu) # Creates a new menu item

    fileMenu.add_command(label='New File') # Created a new item in the fileMenu
    fileMenu.add_command(label='Open File...')
    fileMenu.add_command(label='Open Folder...')

# ******************** submenu of File Tab **************************

    openRecent = Menu(fileMenu, tearoff=0)  # Gets rid of the '----' in the menu
    fileMenu.add_cascade(label='Open Recent', menu=openRecent)
    openRecent.add_cascade(label='Open Recent')

# ******************** File Tab **************************

    fileMenu.add_command(label='Reopen with Encoding')
    fileMenu.add_command(label='View into file')
    fileMenu.add_command(label='Save')
    fileMenu.add_command(label='Save with Encoding')
    fileMenu.add_command(label='Save as...')
    fileMenu.add_command(label='Save All')
    fileMenu.add_separator() # Puts in a clean line without any spacing, '----' without the spacing

    fileMenu.add_command(label='New Window')
    fileMenu.add_command(label='Open Window')
    fileMenu.add_separator()
    fileMenu.add_command(label='Close File')
    fileMenu.add_command(label='Revert File')
    fileMenu.add_command(label='Close All Files')
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=exit)

    editMenu = Menu(menu, tearoff=0) # Same things
    menu.add_cascade(label='Edit', menu=editMenu)
    editMenu.add_command(label='Undo')
    editMenu.add_command(label='Redo')
    editMenu.add_command(label='Undo Selection')
    editMenu.add_separator()
    editMenu.add_command(label='Copy')
    editMenu.add_command(label='Cut')
    editMenu.add_command(label='Paste')
    editMenu.add_command(label='Paste and Indent')
    editMenu.add_command(label='Paste from History')
    editMenu.add_separator()
    editMenu.add_command(label='Line')
    editMenu.add_command(label='Comment')
    editMenu.add_command(label='Text')
    editMenu.add_command(label='Tag')
    editMenu.add_command(label='Mark')
    editMenu.add_command(label='Code Folding')
    editMenu.add_command(label='Convert Case')

    editMenu.add_command(label='Wrap')
    editMenu.add_command(label='Show Completions')
    editMenu.add_separator()
    editMenu.add_command(label='Sort Lines')
    editMenu.add_command(label='Sort Lines (Case Sensitive)')
    editMenu.add_command(label='Permute Lines')
    editMenu.add_command(label='Permute Slections')

    selectionMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Selection', menu=selectionMenu)
    selectionMenu.add_command(label='Split into Lines')
    selectionMenu.add_command(label='Add Previous Line')
    selectionMenu.add_command(label='Add Next Line')
    selectionMenu.add_command(label='Single Selection')
    selectionMenu.add_command(label='Invert Selection')
    selectionMenu.add_separator()
    selectionMenu.add_command(label='Select All')
    selectionMenu.add_command(label='Expand Selection to Line')
    selectionMenu.add_command(label='Expand Selection to Word')

    selectionMenu.add_command(label='Expand Selection to Paragraph')
    selectionMenu.add_command(label='Expand Selection to Scope')
    selectionMenu.add_command(label='Expand Selection to Brackets')
    selectionMenu.add_command(label='Expand Selection to Indentation')
    selectionMenu.add_command(label='Expand slection to Tag')

    findMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Find', menu=findMenu)
    findMenu.add_command(label='Find...')
    findMenu.add_command(label='Find Next')
    findMenu.add_command(label='Find Previous')
    findMenu.add_command(label='Incremental Find')
    findMenu.add_separator()
    findMenu.add_command(label='Replace...')
    findMenu.add_command(label='Replace Next')

    findMenu.add_separator()
    findMenu.add_command(label='Quick Find')
    findMenu.add_command(label='Quick Find All')
    findMenu.add_command(label='Quick Add Next')
    findMenu.add_command(label='Quick Skip Next')
    findMenu.add_separator()
    findMenu.add_command(label='Use Selection for Find')
    findMenu.add_command(label='Use Selection for Replace')
    findMenu.add_separator()
    findMenu.add_command(label='Find in Files...')
    findMenu.add_command(label='Find Results')

# ******************** View Tab **************************

    viewMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='View', menu=viewMenu)

# ******************** submenu of View Tab ***********************

    toolWindows = Menu(viewMenu, tearoff=0)  # Gets rid of the '----' in the menu
    viewMenu.add_cascade(label='Tool Windows', menu=toolWindows)
    toolWindows.add_cascade(label='Project')
    toolWindows.add_cascade(label='Favorites')
    toolWindows.add_cascade(label='Run')
    toolWindows.add_cascade(label='Debug')
    toolWindows.add_cascade(label='TODO')
    toolWindows.add_cascade(label='Structure')
    toolWindows.add_cascade(label='Version Control')
    toolWindows.add_cascade(label='Database')
    toolWindows.add_cascade(label='Event Log')
    toolWindows.add_cascade(label='Python Console')
    toolWindows.add_cascade(label='Terminal')

# ******************** View Tab **************************

    viewMenu.add_command(label='Side Bar')
    viewMenu.add_command(label='Hide Minimap')
    viewMenu.add_command(label='Hide Status Bar')
    viewMenu.add_command(label='Hide Menu')
    viewMenu.add_command(label='Hide Console')
    viewMenu.add_separator()
    viewMenu.add_command(label='Enter Full Screen')
    viewMenu.add_command(label='Enter Distraction Free Mode')
    viewMenu.add_separator()
    viewMenu.add_command(label='Layout')
    viewMenu.add_command(label='Groups')

    viewMenu.add_command(label='Focus Group')
    viewMenu.add_command(label='Move File to Group')
    viewMenu.add_separator()
    viewMenu.add_command(label='Syntax')
    viewMenu.add_command(label='Indentation')
    viewMenu.add_command(label='Line Endings')
    viewMenu.add_separator()
    viewMenu.add_command(label='Word Wrap')
    viewMenu.add_command(label='Word Wrap Column')
    viewMenu.add_command(label='Ruler')
    viewMenu.add_separator()
    viewMenu.add_command(label='Spell Check')
    viewMenu.add_command(label='Next Misspelling')
    viewMenu.add_command(label='Prev Mispelling')
    viewMenu.add_command(label='Dictionary')

    gotoMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Goto', menu=gotoMenu)
    gotoMenu.add_command(label='Goto Anything...')
    gotoMenu.add_separator()
    gotoMenu.add_command(label='Goto Symbol...')
    gotoMenu.add_command(label='Goto Symbol in Project...')
    gotoMenu.add_command(label='Goto Definition...')
    gotoMenu.add_command(label='Goto Line...')
    gotoMenu.add_separator()
    gotoMenu.add_command(label='Jump Back')
    gotoMenu.add_command(label='Jump Forward')
    gotoMenu.add_separator()
    gotoMenu.add_command(label='Switch File')
    gotoMenu.add_separator()
    gotoMenu.add_command(label='Scroll')
    gotoMenu.add_command(label='Bookmarks')
    gotoMenu.add_separator()
    gotoMenu.add_command(label='Jump to Matching Bracket')

    toolsMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Tools', menu=toolsMenu)
    toolsMenu.add_command(label='Command Palette...')
    toolsMenu.add_command(label='Snippets...')
    toolsMenu.add_separator()
    toolsMenu.add_command(label='Build System')
    toolsMenu.add_command(label='Build')

    toolsMenu.add_command(label='Build With...')
    toolsMenu.add_command(label='Cancel Build')
    toolsMenu.add_command(label='Build Results')
    toolsMenu.add_command(label='Save All on Build')
    toolsMenu.add_separator()
    toolsMenu.add_command(label='Record Macro')
    toolsMenu.add_command(label='Playback Macro')
    toolsMenu.add_command(label='Save Macro...')
    toolsMenu.add_command(label='Macros')
    toolsMenu.add_separator()
    toolsMenu.add_command(label='Developer')

    projectMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Project', menu=projectMenu)
    projectMenu.add_command(label='Open Project...')
    projectMenu.add_command(label='Switch Project')
    projectMenu.add_command(label='Quick Switch Project')
    projectMenu.add_command(label='Open Recent')
    projectMenu.add_separator()
    projectMenu.add_command(label='Save Project As...')
    projectMenu.add_command(label='Close Project')
    projectMenu.add_command(label='Edit Project')
    projectMenu.add_separator()
    projectMenu.add_command(label='New Workspace for Project')

    projectMenu.add_command(label='Save Workspace As...')
    projectMenu.add_separator()
    projectMenu.add_command(label='Add Folder to Project...')
    projectMenu.add_command(label='Remove all Folders from Project')
    projectMenu.add_command(label='Refresh Folders')

    preferencesMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Preferences', menu=preferencesMenu)
    preferencesMenu.add_command(label='Browse Packages...')
    preferencesMenu.add_separator()
    preferencesMenu.add_command(label='Settings')
    preferencesMenu.add_command(label='Settings - Syntax Specific')
    preferencesMenu.add_command(label='Settings - Distraction Free')
    preferencesMenu.add_separator()
    preferencesMenu.add_command(label='Key Bindings')
    preferencesMenu.add_separator()
    preferencesMenu.add_command(label='Font')

    preferencesMenu.add_command(label='Color Scheme')
    preferencesMenu.add_separator()
    preferencesMenu.add_command(label='Package Settings')
    preferencesMenu.add_command(label='Package Control')

    helpMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=helpMenu)
    helpMenu.add_command(label='Documentation')
    helpMenu.add_command(label='Twitter')
    helpMenu.add_separator()
    helpMenu.add_command(label='Indexing Status...')
    helpMenu.add_separator()
    helpMenu.add_command(label='Remove License')
    helpMenu.add_separator()

    helpMenu.add_command(label='Check for Updates')
    helpMenu.add_command(label='Changelog...')
    helpMenu.add_command(label='About Sublime Text')

main()

root.title('Sublime Text 3')
app=FullScreenApp()
root.iconbitmap('stx.ico')
root.mainloop()