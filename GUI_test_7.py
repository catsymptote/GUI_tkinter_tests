from tkinter import *


class button_class:
    # "Every time you make a class, you need to blank lines above it" -Bucky.
    # Wat o.O
    def __init__(self, master_window):
        frame = Frame(master_window)
        frame.pack()

        self.print_button = Button(frame, text="Print message", command=self.print_message)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side=LEFT)
    
    def print_message(self):
        print("Here is the printed message.")
        sys.stdout.flush()


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------

b = button_class(root_window)

# Stop ---------------
root_window.mainloop()
# Stop ---------------
