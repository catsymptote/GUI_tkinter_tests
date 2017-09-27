# Python GUI with Tkinter 4, 5
# Grid Layouts, More on the Grid Layouts
# TheNewBoston


from tkinter import *


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


label_one = Label(root_window, text="Name")
label_two = Label(root_window, text="Password")
entry_1 = Entry(root_window)
entry_2 = Entry(root_window)

label_one.grid(row=0, sticky=E) # sticky=E is go left (E for East)
label_two.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

checkbox_one = Checkbutton(root_window, text="Keep me signed in")

checkbox_one.grid(columnspan=2, row=2)


# Stop ---------------
root_window.mainloop()
# Stop ---------------
