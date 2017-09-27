from tkinter import *


def do_nothing():
    print("You clicked a button or whatever")
    sys.stdout.flush()


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------



""" ***** Main Menu ***** """
# Main menu
main_menu = Menu(root_window)
root_window.config(menu=main_menu)

# First sub menu - File
sub_menu_1 = Menu(main_menu)
main_menu.add_cascade(label="File", menu=sub_menu_1)

sub_menu_1.add_command(label="New", command=do_nothing)
sub_menu_1.add_command(label="Open", command=do_nothing)
sub_menu_1.add_separator()
sub_menu_1.add_command(label="Save", command=do_nothing)
sub_menu_1.add_command(label="Save As", command=do_nothing)
sub_menu_1.add_separator()
sub_menu_1.add_command(label="Exit", command=do_nothing)

# Second sub menu - Edit
sub_menu_2 = Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=sub_menu_2)

sub_menu_2.add_command(label="Undo", command=do_nothing)
sub_menu_2.add_command(label="Redo", command=do_nothing)
sub_menu_2.add_separator()
sub_menu_2.add_command(label="Cut", command=do_nothing)
sub_menu_2.add_command(label="Copy", command=do_nothing)
sub_menu_2.add_command(label="Paste", command=do_nothing)



""" ***** Toolbar ***** """
# Make toolbar
toolbar = Frame(root_window, bg="blue")

# Add elements to the toolbar
insert_butt = Button(toolbar, text="Insert Image", command=do_nothing)
insert_butt.pack(side=LEFT, padx=2, pady=2)
print_butt = Button(toolbar, text="Print", command=do_nothing)
print_butt.pack(side=LEFT, padx=2, pady=2)

# Pack the toolbar
toolbar.pack(side=TOP, fill=X)



""" ***** Statusbar ***** """
statusbar = Label(root_window, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)



# Stop ---------------
root_window.mainloop()
# Stop ---------------
