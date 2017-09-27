from tkinter import *
import tkinter.messagebox


# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


# Basic info messagebox
tkinter.messagebox.showinfo("Da Title, Man", "Monkeys can live up to 300 years.")


# Yes/no messagebox
answer = tkinter.messagebox.askquestion("Question 1", "Can monkeys can live up to 300 years?")

if (answer == "yes"):
    print("You are wrong, silly :P")
    sys.stdout.flush()
else:
    print("Good shit, man")
    sys.stdout.flush()


# Stop ---------------
root_window.mainloop()
# Stop ---------------
