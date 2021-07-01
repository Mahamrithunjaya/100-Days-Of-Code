from tkinter import *
from tkcalendar import *
from datetime import datetime as dt
import requests
import webbrowser
from tkinter import messagebox
import os

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{os.environ.get('USER_NAME')}/graphs"

window = Tk()
window.title("Coding Tracker")
window.iconphoto(True, PhotoImage(file="images/coding.png"))
window.resizable(width=False, height=False)
window.config(pady=20, padx=20)
URL = f"{graph_endpoint}/codinghabit"
TODAY = dt.now()


def open_browser():
    webbrowser.open(URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    endpoint = f"{graph_endpoint}/{os.environ.get('GRAPH_ID')}"
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    requests.post(url=endpoint, json=pixel_add, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="Pixel Added Successfully.")


def delete_pixel():
    endpoint = f"{graph_endpoint}/{os.environ.get('GRAPH_ID')}/{format_date()}"
    requests.delete(url=endpoint, headers=headers)
    messagebox.showinfo(message="DONE.\nPixel Deleted.")


def change_pixel():
    endpoint = f"{graph_endpoint}/{os.environ.get('GRAPH_ID')}/{format_date()}"
    pixel_update = {
        "quantity": user_in.get()
    }
    requests.put(url=endpoint, json=pixel_update, headers=headers)
    user_in.delete(0, END)
    messagebox.showinfo(message="CHANGED SUCCESSFULLY.\nPixel updated.")


cal = Calendar(window, selectmode="day", year=TODAY.year, month=TODAY.month, day=TODAY.day)
cal.grid(row=0, column=0, columnspan=4)
units = Label(text="Hours/Day: ")
units.grid(row=1, column=0, columnspan=2, pady=10, sticky=E)
user_in = Entry(width=10)
user_in.grid(row=1, column=2, sticky=W)


headers = {
    "X-USER-TOKEN": "PERSONAL_TOKEN"
}
graph_parameters = {
    "id": os.environ.get("GRAPH_ID"),
    "name": "Coding Tracker",
    "unit": "Hour",
    "type": "float",
    "color": "shibafu"
}

add = Button(text="ADD", command=add_pixel)
add.grid(row=2, column=0, pady=10)
update = Button(text="UPDATE", command=change_pixel)
update.grid(row=2, column=1, pady=10, sticky=W)
delete = Button(text="DELETE", command=delete_pixel)
delete.grid(row=2, column=2, pady=10, sticky=W)
link = Button(text="Show\nJourney", command=open_browser)
link.grid(row=2, column=3)

window.mainloop()
