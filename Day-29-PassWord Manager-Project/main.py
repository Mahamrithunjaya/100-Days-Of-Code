from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from tkinter.ttk import *
# from intro_window import IntroWindow
# import generate


# ---------------------------------------------- PASSWORD GENERATOR ------------------------------------------------ #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '[', ']', '?', '=', ':', ';']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(5, 8))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 6))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # popup = generate.PopupGenerator(window)
    # password = popup.password

    if len(password_input.get()) == 0:
        password_input.insert(0, password)
    else:
        password_input.delete(0, END)
        password_input.insert(0, password)
    pyperclip.copy(password)

    print(f"Your password is: {password}")


# ------------------------------------------------ SAVE PASSWORD --------------------------------------------------- #
def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email/username": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                if website in data:
                    update = messagebox.askyesno(title="WARNING ❗❗",
                                                 message=f"There is already a password saved for {website}."
                                                         f"\nWould you like to overwrite?")
                    if update:
                        data[website]['password'] = password
                        data[website]['email/username'] = email
                    else:
                        return
                else:
                    # Updating old data with new data
                    data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ------------------------------------------------- CLEAR ENTRIES --------------------------------------------------- #
def clear_entries():
    website_input.delete(0, END)
    password_input.delete(0, END)
    email_input.delete(0, END)


# ------------------------------------------------- FIND PASSWORD --------------------------------------------------- #
def find_password():
    website = website_input.get()
    if len(website) != 0:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                user_data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showerror(title="FILE NOT FOUND ERROR !!",
                                 message="No Data File Found.\n\nSolution: Please add some data and save passwords "
                                         "to search.")
        else:
            if website in user_data:
                email = user_data[website]['email/username']
                password = user_data[website]['password']
                pyperclip.copy(password)
                messagebox.showinfo(title=website, message=f"Email/Username: {email}\n\nPassword: {password}\n\n"
                                                           f"Note: Your password is copied to clipboard.")
            else:
                messagebox.showinfo(title="ERROR !!! NOT FOUND",
                                    message=f"No details for {website} exists in data file.")


# ------------------------------------------------ Menu Functions --------------------------------------------------- #
def format_data(new_window):
    pass_buttons = []
    passwords = []
    emails = []
    websites = []
    web_r = 1
    em_r = 1
    pas_r = 1
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError or FileNotFoundError:
        if_no = Label(new_window, text="No Saved Data or Passwords found\nAdd Passwords to view them.",
                      font=("Roboto", 20, "bold"))
        if_no.grid(row=1, column=0, columnspan=3, pady=20)
    else:
        for website in data:
            websites.append(website)
            emails.append(data[website]["email/username"])
            passwords.append(data[website]["password"])
        for website in websites:
            websites_label = Label(new_window, text=website)
            websites_label.grid(column=0, row=web_r, pady=5)
            web_r += 1
        for email in emails:
            emails_label = Label(new_window, text=email)
            emails_label.grid(column=1, row=em_r, padx=20, pady=5)
            em_r += 1

        def copy_pass(password_to_copy):
            pyperclip.copy(password_to_copy)

        for password in passwords:
            pas_button = Button(new_window, text=password, width=30)
            pas_button.config(command=lambda password_arg=pas_button: copy_pass(password_arg.cget('text')))
            pas_button.grid(column=2, row=pas_r, padx=15, pady=5)
            pas_r += 1
            pass_buttons.append(pas_button)

    new_window.mainloop()


# -------------------------------------------- VIEWING SAVED PASSWORDS ---------------------------------------------- #
def view_saved():
    new_window = Tk()
    new_window.title("Saved Passwords")
    new_window.config(padx=30, pady=30)

    styles = Style(new_window)
    new_window.tk.call('source', 'azure-dark.tcl')
    styles.theme_use('azure-dark')

    web_label = Label(new_window, text="WEBSITES", foreground="red", font=("Roboto", 10, "bold"))
    web_label.grid(column=0, row=0)
    email_user_label = Label(new_window, text="EMAIL / USERNAME", foreground="red", font=("Roboto", 10, "bold"))
    email_user_label.grid(column=1, row=0)
    pas_label = Label(new_window, text="PASSWORD (Click to Copy)", foreground="red", font=("Roboto", 10, "bold"))
    pas_label.grid(column=2, row=0)
    format_data(new_window)


# --------------------------------------------------- UI SETUP ------------------------------------------------------ #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

style = Style(window)
window.tk.call('source', 'azure-dark.tcl')
style.theme_use('azure-dark')

# ------------------------------- Canvas -----------------------------#
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ------------------------------ Labels --------------------------------#
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0, )

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, )

# ------------------------------ Entries ------------------------------ #
website_input = Entry()
website_input.grid(row=1, column=1, sticky="EW", padx=3, pady=3)
website_input.focus()

email_input = Entry()
email_input.grid(row=2, column=1, columnspan=2, sticky="EW", padx=3, pady=3)
email_input.insert(0, "markzuckerbarg@gmail.com")

password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW", padx=3, pady=3)

# ------------------------------- Buttons ----------------------------- #
generate_password_button = Button(text="Generate Password", command=generate_password, state=ACTIVE)
generate_password_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="ADD", width=36, command=save_data, state=ACTIVE)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", pady=10, padx=5)

clear_button = Button(text="CLEAR", width=12, command=clear_entries)
clear_button.grid(row=4, column=0)

search_button = Button(text="SEARCH", command=find_password)
search_button.grid(row=1, column=2, stick="EW")

# ------------------------------- Menu Bar -------------------------------- #
menu_bar = Menu(window)
options = Menu(menu_bar, tearoff=0)
options.add_command(label="Saved Passwords", command=view_saved)
options.add_command(label="Back")

options.add_separator()

options.add_command(label="Exit", command=window.quit)

menu_bar.add_cascade(label="Options", menu=options)
window.config(menu=menu_bar)

window.mainloop()
