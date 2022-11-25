from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)
    
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_input = website_entry.get()
    login_input = login_entry.get()
    password_input = password_entry.get()
    
    if len(website_input) == 0 or len(password_input) == 0 or len(login_input) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f'These are details that you entered: '
                                                                    f'\nEmail: {login_input}'
                                                                    f'\nPassword: {password_input} '
                                                                    f'\nIs it ok to save?')
        if is_ok:
            with open("data.txt", 'a') as f:
                f.write(f'{website_input} | {login_input} | {password_input}\n')
                website_entry.delete(0, END)
                login_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

login_label = Label(text='Email/Username:')
login_label.grid(column=0, row=2)
login_entry = Entry(width=52)
login_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)
generate_password = Button(text='Generate Password', command=generate_password)
generate_password.grid(column=2, row=3)

add_btn = Button(width=44, text='Add', command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()