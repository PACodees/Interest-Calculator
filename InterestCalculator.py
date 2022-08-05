from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Interest Calculator")

compoundType = StringVar()
def calculate():
    global period
    if len(principalEntry.get()) == 0 or len(rateEntry.get()) == 0 or len(compoundType.get()) == 0 or len(timeEntry.get()) == 0:
        errorbox = messagebox.showwarning("Error", "One or more querys have not been filled out. Please try again.")
        return
    if compoundType.get() == "Annually":
        period = 1
    if compoundType.get() == "Semiannually":
        period = 2
    if compoundType.get() == "Quarterly":
        period = 4
    if compoundType.get() == "Monthly":
        period = 12
    P = float(principalEntry.get())
    r = float(rateEntry.get())/100
    t = float(timeEntry.get())
    n = float(period)
    balance = P*(1 + r/n)**(n*t)
    successbox = messagebox.showinfo("Result", f"End balance: {balance}")
Label(root, text="Starting Principal").grid(row=0, column=0)
principalEntry = Entry(root)
principalEntry.grid(row=0, column=1)
Label(root, text="Interest Rate").grid(row=1, column=0)
rateEntry = Entry(root)
rateEntry.grid(row=1, column=1)
Label(root, text="Compound").grid(row=2, column=0)
compound_drop_down = OptionMenu(root, compoundType, "Annually", "Semiannually", "Quarterly", "Monthly")
compound_drop_down.grid(row=2, column=1)
Label(root, text="After (years)").grid(row=3, column=0)
timeEntry = Entry(root)
timeEntry.grid(row=3, column=1)
Button(root, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2)

root.mainloop()