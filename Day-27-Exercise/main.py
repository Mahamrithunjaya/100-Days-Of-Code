import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am A Label", font=("Courier", 35, "bold"))
my_label.grid(column=0, row=0)

# Button


def button1_clicked():
    print("I got Clicked!")
    # my_label.config(text=input_entry.get())


button1 = tkinter.Button(text="Button 1", command=button1_clicked)
button1.grid(column=1, row=1)


def button2_clicked():
    print("I got Clicked!")


button2 = tkinter.Button(text="New_Button", command=button2_clicked)
button2.grid(column=2, row=0)

# Entry

input_entry = tkinter.Entry(width=25)
input_entry.grid(column=3, row=2)


window.mainloop()

# def add(*args):
#     addition = 0
#     for n in args:
#         addition += n
#     return addition
#
#
# print(add(1, 2, 3, 4, 5, 6, 7))
#

# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
#
# my_car = Car(make="Nissan")


# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)
