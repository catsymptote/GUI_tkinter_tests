# Python GUI with Tkinter 6
# Binding Functions to Layouts
# TheNewBoston


from tkinter import *
import test_file
import sys


def button_1_function():
    test_file.printer1()

def button_2_function(event):
    test_file.printer2("ello")


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


#test_file.printer1()   # Prints "hi"
#test_file.printer2("Hello")    # Prints passed parameter

button_1 = Button(root_window, text="printer1()", command=button_1_function)
button_1.pack()

# TypeError: 'Button' object is not callable
"""
button_2 = Button(root_window, text="printer2()")
button_2.bind("<Button-1>", button_2)
button_2.pack()
"""


# Stop ---------------
root_window.mainloop()
# Stop ---------------
