from tkinter import *


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


# Make the canvas to draw on
canvas_1 = Canvas(root_window, width=800, height=400)
canvas_1.pack()

# Draw lines ++
blackline_1 = canvas_1.create_line(10, 10, 790, 200)
blackline_2 = canvas_1.create_line(790, 200, 10, 390)
blackline_3 = canvas_1.create_line(10, 10, 10, 390)
redline_1 = canvas_1.create_line(10, 200, 790, 200, fill="red")

greenbox = canvas_1.create_rectangle(20, 100, 350, 300, fill="green")

# Delete functions
"""
canvas_1.delete(redline_1)
canvas_1.delete(ALL)
"""


# Stop ---------------
root_window.mainloop()
# Stop ---------------
