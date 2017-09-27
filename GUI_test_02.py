from tkinter import *


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


# Make frames
top_div = Frame(root_window)
top_div.pack()

bottom_div = Frame(root_window)
bottom_div.pack(side=BOTTOM)


# Button widget
button1 = Button(top_div,       text="< Button 1 >", fg="red")   # fg parameter is foreground color (optional)
button2 = Button(top_div,       text="< Button 2 >", fg="brown")
button3 = Button(top_div,       text="< Button 3 >", fg="blue")
button4 = Button(bottom_div,    text="< Button 4 >", fg="green")

# Pack buttons
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()


# Stop ---------------
root_window.mainloop()
# Stop ---------------
