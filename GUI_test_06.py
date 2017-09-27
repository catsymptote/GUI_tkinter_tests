# Python GUI with Tkinter 7
# Mouse Click Events
# TheNewBoston

from tkinter import *
import sys
import test_file


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


def left_click(event):
    print("Left")
    sys.stdout.flush()

def middle_click(event):
    print("Middle")
    sys.stdout.flush()

def right_click(event):
    print("Right")
    sys.stdout.flush()


frame = Frame(root_window, width=300, height=250)
frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)
frame.pack()


# Stop ---------------
root_window.mainloop()
# Stop ---------------
