from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    final_password = "".join(password_list)

    Input3.insert(index=0, string=final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = Input1.get()
    email_entry = Input2.get()
    password_entry = Input3.get()
    new_data = {website_entry: {
        "email": email_entry,
        "password": password_entry
    }
    }

    if website_entry == "" or password_entry == "":
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty")
    else:
        try:
            with open("data.json", "r") as data:
                # reading the data
                json_data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                # updating the data
                json.dump(new_data, data, indent=4)
        else:
            # saving the data
            json_data.update(new_data)

            with open("data.json", "w") as data:
                json.dump(json_data, data, indent=4)
        finally:
            Input1.delete(0, "end")
            Input3.delete(0, "end")


def find_password():
    website_entry = Input1.get()
    try:
        with open("data.json", "r") as data:
            json_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")
    else:
        if website_entry in json_data:
            found_password = json_data[website_entry]['password']
            messagebox.showinfo(title=website_entry, message=f"website's name : {website_entry}\n "
                                                             f"Password : {found_password}")
        else:
            messagebox.showinfo(title="error", message=f"No details for {website_entry} exists.")


# ---------------------------- UI SETUP ------------------------------- #


page = Tk()
page.config(padx=20, pady=20)
page.title("password manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
website.focus()

# enter the website name
Input1 = Entry(width=33)
Input1.grid(column=1, row=1, columnspan=1)

Email = Label(text="Email/Username:")
Email.grid(row=2, column=0)

# enter the Email/Username
Input2 = Entry(width=53)
Input2.grid(column=1, row=2, columnspan=2)
Input2.insert(0, 'vedantpant@gmail.com')

Password = Label(text="Password:")
Password.grid(row=3, column=0)

# enter the password
Input3 = Entry(width=33)
Input3.grid(column=1, row=3)

# button generate password
password = Button(text="Generate Password", command=password_generator)
password.config(width=16)
password.grid(column=2, row=3)

# button add
add = Button(text="Add", command=save)
add.config(width=45)
add.grid(column=1, row=4, columnspan=2)

# button search
search = Button(text="Search", command=find_password)
search.config(width=16)
search.grid(column=2, row=1)

page.mainloop()
