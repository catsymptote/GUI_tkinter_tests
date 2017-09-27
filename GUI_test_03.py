from tkinter import *


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


one = Label(root_window, text="One", bg="red", fg="white")
one.pack(side=LEFT, fill=Y)
two = Label(root_window, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root_window, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)
four = Label(root_window, text="Four", bg="brown", fg="white")
four.pack(side=LEFT)


# Stop ---------------
root_window.mainloop()
# Stop ---------------
