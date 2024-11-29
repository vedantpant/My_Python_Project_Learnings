import tkinter
# from tkinter import END

window = tkinter.Tk()

window.title("my first GUI program.")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    my_label.config(text=Input.get(), font=("Ariel", 8, "bold"))


def second_button_clicked():
    my_label.config(text="it is a second click", font=("Ariel", 10, "bold"))


# Creating label
my_label = tkinter.Label(text="New Text", font=("Ariel", 8, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)
my_label.config(padx=5, pady=5)

# button
button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=2)
button1 = tkinter.Button(text="click me also", command=second_button_clicked)
button1.grid(column=3, row=1)

# entry component
Input = tkinter.Entry(width=30)
Input.insert(index=0, string="SOMETHING TO START WITH.")
Input.grid(column=4, row=4)

# # text box
# textbox = tkinter.Text(height=5, width=30)
# textbox.focus()
# textbox.insert(END, "Example of multiline text entry.")
# print(textbox.get("1.0", END))
# textbox.pack()
#
#
# # spinbox
#
#
# def spinbox_used():
#     print(spinbox.get())
#
#
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # scale
# def scale_used(value):
#     print(value)
#
#
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # checkbox
#
#
# def checkbox_used():
#     print(checked_state.get())
#
#
# checked_state = tkinter.IntVar()
# checkbox = tkinter.Checkbutton(text="Is it on??", variable=checked_state, command=checkbox_used)
# checked_state.get()
# checkbox.pack()
#
# # radio button
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# radio_state = tkinter.IntVar()
# radio_button_1 = tkinter.Radiobutton(text="option 1", value=1, variable=radio_state, command=radio_used)
# radio_button_2 = tkinter.Radiobutton(text="option 2", value=2, variable=radio_state, command=radio_used)
# radio_button_1.pack()
# radio_button_2.pack()
#
#
# # listbox
# def listbox_used(event):
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = tkinter.Listbox(height=10)
# fruits = ["apple", "mangoes", "guava", "grapes"]
# for fruit in fruits:
#     listbox.insert(fruits.index(fruit), fruit)
#
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()
