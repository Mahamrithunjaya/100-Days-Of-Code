from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json

# ----------------------------Variables------------------------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

pass_text = ""
note_text = ""
btn_text = ""


# --------------------------------Security check------------------------------------#
def intro(is_first):
    global pass_text, note_text, btn_text
    if is_first:
        pass_text = "Choose Password: "
        note_text = "This password is required to unlock this app.\n\nNote:1)Remember Password\n" \
                    "2)Choose strong Password\nConform Password?"
        btn_text = "Save"


def check_json_data():
    with open("appdata.json") as appdata:
        data = json.load(appdata)
        is_first_time = data["is_first_time"]
    if is_first_time == "True":
        intro(True)
        with open("appdata.json") as appdata:
            data = json.load(appdata)
        data["is_first_time"] = "False"
        with open("appdata.json", 'w') as file_appdata:
            json.dump(data, file_appdata)
    else:
        intro(False)


class IntroWindow:

    def __init__(self):
        self.check_first(intro)
        self.pass_text = "Password"
        self.note_text = ""
        self.btn_check = "Check"

        # Window
        self.intro_win = Tk()
        self.intro_win.title("Setup")
        self.intro_win.geometry("500x500")
        self.style = Style(self.intro_win)
        self.intro_win.tk.call('source', 'azure-dark.tcl')
        self.style.theme_use('azure-dark')

        # Canvas
        self.logo_canvas = Canvas()
        self.intro_img = PhotoImage(file="intro_img.png")
        self.logo_canvas.create_image(180, 180, image=self.intro_img)
        self.logo_canvas.place(x=0, y=0)

        # Labels
        self.name = Label(text="DARK-KNIGHT GRADE SECURITY")
        self.name.config(foreground="orange", font=("Roboto", 20, "bold"))
        self.name.place(x=60, y=10)

        self.note_info = Label(text=self.note_text)
        self.note_info.config(foreground="red", font=("aerial", 8, "bold"))
        self.note_info.place(x=3, y=340)

        self.pass_info = Label(text=self.pass_text)
        self.pass_info.config(foreground="green", font=("aerial", 10, "bold"))
        self.pass_info.place(x=5, y=280)

        # TextField
        self.entry = Entry(width=30)
        self.entry.place(x=130, y=280)

        self.store_pass()
        self.security_chek()

        self.intro_win.mainloop()

    def store_pass(self):
        response = messagebox.askyesno(title="Conform Password",
                                       message=self.note_text)
        if response:
            update_info = {"password": self.entry.get()}
            print(len(update_info["password"]))
            if len(update_info["password"]) > 0:
                if update_info["password"][0] != " ":
                    with open("appdata.json") as app_info:
                        data = json.load(app_info)
                        data.update(update_info)
                    with open("appdata.json", 'w') as app_info:
                        print(data["password"])
                        data["password"] = self.entry.get()
                        json.dump(data, app_info)
                    self.entry.delete(0, END)
                    self.intro_win.destroy()

    def security_chek(self):
        with open("appdata.json") as file:
            password = json.load(file)["password"]
            if self.entry.get() == password:
                self.intro_win.destroy()
            else:
                messagebox.showwarning(title="Bad Password.", message="The Password you entered was not correct one.")
                quit()

    def check_first(self, is_first):
        if is_first:
            save_btn = Button(text=btn_text, width=15, command=self.store_pass)
        else:
            save_btn = Button(text=btn_text, width=15, command=self.security_chek)
            print("Passed")
        save_btn.place(x=160, y=310)
