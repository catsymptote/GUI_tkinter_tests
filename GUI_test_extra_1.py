# Python GUI with Tkinter
# Interaction with Checkboxes, entries ++
# Catsymptote


from tkinter import *
import sys


def output_thingy():
    if(checkbox_one_check.get()):
        print("Checked")
        print(checkbox_one_check.get())
        print(entry_1.get())
        sys.stdout.flush()
    else:
        print("Unchecked")
        print(checkbox_one_check.get())
        print(entry_2.get())
        sys.stdout.flush()



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

done_button = Button(root_window, text="< Done >", fg="green", command=output_thingy)
done_button.grid(columnspan=2, row=3)

checkbox_one_check = IntVar()
checkbox_one = Checkbutton(root_window, text="Keep me signed in", variable=checkbox_one_check)
checkbox_one.grid(columnspan=2, row=2)


# Stop ---------------
root_window.mainloop()
# Stop ---------------
