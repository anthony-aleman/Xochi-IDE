from tkinter import *
from tkinter import ttk
import subprocess
from tkinter.filedialog import asksaveasfile, askopenfilename
from tkinter.scrolledtext import ScrolledText

# instance for window
ide_window = Tk()
ide_window.title('Xochi')

# creating the menubar
menu_bar = Menu(ide_window)
ide_window.config(menu=menu_bar)

# adding file menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New File')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=ide_window.destroy)

# adding edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Delete')

# adding help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Tk Help')
help_menu.add_command(label='Demo')
help_menu.add_command(label='Contact Me')


# editor for code
ide_editor_window = ScrolledText(ide_window, font='haveltica 10 bold', wrap=None)
ide_editor_window.pack(fill=BOTH, expand=1)
ide_editor_window.focus()

if __name__ == '__main__':
    ide_window.mainloop()
