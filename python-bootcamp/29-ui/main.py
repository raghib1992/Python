# ref Link
# https://tkdocs.com/tutorial/canvas.html

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)
    password = ''.join(password_list)
    # Once password is generated, it is copy to clipborad
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    websites = entry_websites.get()
    user = entry_user.get()
    password = entry_password.get()

    # message Box before tput info on text file
    # messagebox.showinfo(title="Title", messagge="Message")

    if len(websites) == 0 and len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    else: 
        is_ok = messagebox.askokcancel(title=websites, message=f"These are the detials entered: \nEmail: {user}\nPassword: {password} \nIs it OK to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{websites} | {user} | {password}\n")
                entry_websites.delete(0, END)
                entry_password.delete(0,END)
    return

# ---------------------------- UI SETUP ------------------------------- #
# Create window using Tk() from tkinter
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)


# Upload photo on window using canvas class
canvas = Canvas(width=300, height=300, highlightthickness=2)
logo_img = PhotoImage(file="logo.png") 
canvas.create_image(150,150,image=logo_img)
canvas.grid(column=1,row=0)

# Add Text and button and block for input
label_websites = Label(text="websites:", font=(FONT_NAME, 24))
label_websites.grid(row=1, column=0)

entry_websites = Entry(width=65)
entry_websites.grid(row=1,column=1, columnspan=2)
entry_websites.focus()


label_user = Label(text= "Email/Username:", font=(FONT_NAME, 24))
label_user.grid(row=2, column=0)

entry_user = Entry(width=65)
entry_user.grid(row=2,column=1,columnspan=2)
entry_user.insert(0, "raghib@raghibnadim.com")


label_password = Label(text= "Password:", font=(FONT_NAME, 24))
label_password.grid(row=3, column=0)

entry_password = Entry(width=45)
entry_password.grid(row=3,column=1)

button_password = Button(text="Generate Password",command=generate_password)
button_password.grid(row=3,column=2)

button_add = Button(text="Add",width= 62, command=add)
button_add.grid(row=4,column=1, columnspan=2)


window.mainloop()

