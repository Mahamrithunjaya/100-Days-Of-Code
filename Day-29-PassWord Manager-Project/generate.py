from tkinter import *
from random import randint, choice, shuffle

TITLE_FONT = ("Roboto", 18, "bold")
PWD_FONT = ("Montserrat", 12, "bold")
NORMAL_FONT = ("Roboto", 10, "normal")
LARGE_FONT = ("Roboto", 12, "normal")

uppercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z']
lowercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                     'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '[', ']', '?', '=', ':', ';']


class PopupGenerator:
    """Creates a new popup window containing the widgets allowing the user to create a random password"""
    global uppercase_letters, lowercase_letters, numbers, symbols

    def __init__(self, master):
        # Define Variables
        self.password = ""
        self.password_length = 16
        self.password_upper = 1
        self.password_lower = 1
        self.password_number = 0
        self.password_symbol = 0
        self.password_number_qty = 4
        self.password_symbol_qty = 2
        self.qty_lower = 0
        self.list_password = []
        self.remaining = 16

        # UI Setup
        self.popup = Toplevel(master)
        self.popup.title("Password Generator")
        self.popup.config(padx=30, pady=30)

        self.length_pwd = IntVar()
        self.check_upper = IntVar()
        self.check_upper.set(1)  # Default to check
        self.check_lower = IntVar()
        self.check_lower.set(1)  # Default to check
        self.check_number = IntVar()
        self.check_symbol = IntVar()

        self.label_title = Label(self.popup, text="Password Generator", pady=5, fg="dark green", font=TITLE_FONT)
        self.label_password = Label(self.popup, text="Password", width=20, height=3, relief=SUNKEN, bg="#cccccc",
                                    fg="blue", font=PWD_FONT, wraplength=200)
        self.scale_length = Scale(self.popup, label="Password Length", from_=6, to=48, length=200, font=NORMAL_FONT,
                                  orient=HORIZONTAL, command=self.scale)
        self.checkbox_upper = Checkbutton(self.popup, text="Use A-Z", selectcolor="red", font=NORMAL_FONT, variable=self.check_upper,
                                          command=self.do_it)
        self.checkbox_lower = Checkbutton(self.popup, text="Use a-z", selectcolor="red", font=NORMAL_FONT, variable=self.check_lower,
                                          command=self.do_it)
        self.checkbox_number = Checkbutton(self.popup, text="Use 0-9", selectcolor="red", font=NORMAL_FONT, variable=self.check_number,
                                           command=self.do_it)
        self.checkbox_symbol = Checkbutton(self.popup, text="Use !@#$%^&*", selectcolor="red", font=NORMAL_FONT,
                                           variable=self.check_symbol, command=self.do_it)
        self.spinbox_number = Spinbox(self.popup, from_=1, to=9, width=3, font=LARGE_FONT, command=self.do_it)
        self.spinbox_symbol = Spinbox(self.popup, from_=1, to=9, width=3, font=LARGE_FONT, command=self.do_it)
        self.label_number = Label(self.popup, text="How many numbers", font=NORMAL_FONT, pady=5)
        self.label_symbol = Label(self.popup, text="How many symbols", font=NORMAL_FONT, pady=5)
        self.button_close = Button(self.popup, text="Close", font=NORMAL_FONT, command=self.close)

        self.scale_length.set(self.password_length)

        # ------------------------------    LAYOUT    ------------------------------ #

        self.label_title.grid(row=0, column=0, columnspan=3)
        self.label_password.grid(row=1, column=0, columnspan=3)
        self.scale_length.grid(row=2, column=0, columnspan=3)
        self.checkbox_upper.grid(row=3, column=1, sticky=W)
        self.checkbox_lower.grid(row=4, column=1, sticky=W)
        self.checkbox_number.grid(row=5, column=1, sticky=W)
        self.checkbox_symbol.grid(row=6, column=1, sticky=W)
        self.label_number.grid(row=7, column=0, columnspan=2)
        self.spinbox_number.grid(row=7, column=2)
        self.label_symbol.grid(row=8, column=0, columnspan=2)
        self.spinbox_symbol.grid(row=8, column=2)
        self.button_close.grid(row=9, column=0, columnspan=3)

        self.popup.mainloop()

    def scale(self, val):
        # This routine is required because Scale() passes one string value to the called function.
        self.password_length = int(val)
        self.do_it()

    def do_it(self):
        """Create the password every time a widget is altered"""
        self.password = ""  # Clear out any existing password
        self.remaining = self.password_length  # Number of characters in password yet to be filled

        # Get current values of checkboxes and spinboxes
        self.password_upper = self.check_upper.get()
        self.password_lower = self.check_lower.get()
        self.password_number = self.check_number.get()
        self.password_symbol = self.check_symbol.get()
        self.password_number_qty = int(self.spinbox_number.get())
        self.password_symbol_qty = int(self.spinbox_symbol.get())

        # Restrict numbers and symbols to half the password length
        if self.password_number:
            self.spinbox_number["to"] = self.password_length // 2
        if self.password_symbol:
            self.spinbox_symbol["to"] = self.password_length // 2

        # Generate the password
        if self.password_symbol:
            for _ in range(0, self.password_symbol_qty):
                self.password += choice(symbols)
            self.remaining = self.password_length - len(self.password)
        if self.password_number:
            for _ in range(0, self.password_number_qty):
                self.password += choice(numbers)
            self.remaining = self.password_length - len(self.password)
        if self.password_lower and self.remaining > 0:
            if self.password_upper:
                self.qty_lower = randint(1, self.remaining)
            else:
                self.qty_lower = self.remaining
            for _ in range(1, self.qty_lower):
                self.password += choice(lowercase_letters)
            self.remaining = self.password_length - len(self.password)
        if self.password_upper and self.remaining > 0:
            for _ in range(0, self.remaining):
                self.password = self.password + choice(uppercase_letters)

        self.list_password = list(self.password)
        shuffle(self.list_password)
        self.password = "".join(self.list_password)
        self.label_password["text"] = self.password

    def close(self):
        self.popup.quit()  # This allows the password to be accessed by main.py
        self.popup.destroy()  # Then destroy this script window
