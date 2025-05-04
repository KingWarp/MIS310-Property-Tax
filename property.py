#Group 1
#Not AI version

import tkinter as tk
from tkinter import messagebox

def calculate_tax():
    try:
        inputvalue = float(actual_value_entry.get())

        assessmentvalue = inputvalue * 0.60

        propertytax = (assessmentvalue / 100) * 0.75


        assessmentvaluelabel.config(text=f"Assessment Value: ${assessmentvalue:.2f}")
        propertytaxlabel.config(text=f"Property Tax: ${propertytax:.2f}")

    except ValueError:

        messagebox.showerror("Invalid Input")


window = tk.Tk()
window.title("Property Tax Calculator")

inputvalue = tk.Label(window, text="How much is the property worth: ")
inputvalue.pack()

actualvalue_entry = tk.Entry(window)
actualvalue_entry.pack()

calculatebutton = tk.Button(window, text="Calculate", command=calculatetax)
calculatebutton.pack()

assessmentvaluelabel = tk.Label(window, text="The land's Evaluation is: $0.00")
assessmentvaluelabel.pack()

propertytaxlabel = tk.Label(window, text="The property tax due is: $0.00")
propertytaxlabel.pack()

window.mainloop()
