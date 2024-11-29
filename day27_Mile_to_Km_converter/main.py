import tkinter
from tkinter import END

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

# configure the words
label1 = tkinter.Label(text="is equal to", font=("Ariel", 15))
label1.grid(column=1, row=2)
label2 = tkinter.Label(text="Miles", font=("Ariel", 15))
label2.grid(column=3, row=1)
label3 = tkinter.Label(text="Km", font=("Ariel", 15))
label3.grid(column=3, row=2)
label1.config(padx=10)
label2.config(padx=10)
label3.config(padx=10)

# Input the miles
Input = tkinter.Text(height=1, width=10)
Input.grid(column=2, row=1)


def miles_to_km():
    miles = Input.get(1.0, END)
    miles = miles.strip(" ")
    km = float(miles) * 1.6
    label4 = tkinter.Label(text=km, font=("Ariel", 15))
    label4.grid(column=2, row=2)
    label4.config(padx=10)


# button for calculate
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()
