# Python GUI with Tkinter 14
# Images and Icons
# TheNewBoston


from tkinter import *


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


photo_1 = PhotoImage(file="img/img_1.png")
label_1 = Label(root_window, image=photo_1)
label_1.pack()

photo_2 = PhotoImage(file="img/img_2.png")
label_2 = Label(root_window, image=photo_2)
label_2.pack()


# Stop ---------------
root_window.mainloop()
# Stop ---------------
