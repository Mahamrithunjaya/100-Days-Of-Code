from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)


def calculate_conversion():
    try:
        if radio_state.get() == 1:
            miles = float(convert_entry.get())
            kilo_meters = round(miles * 1.609, 4)
            label3.config(text=f"{kilo_meters}")

        elif radio_state.get() == 2:
            centimeter = float(convert_entry.get())
            meter = round(centimeter / 100, 3)
            label3.config(text=f"{meter}")

        elif radio_state.get() == 3:
            meters = float(convert_entry.get())
            inch = round(meters * 39.37, 3)
            label3.config(text=f"{inch}")

        elif radio_state.get() == 4:
            foot = float(convert_entry.get())
            inches = round(foot * 12, 3)
            label3.config(text=f"{inches}")
        else:
            label3.config(text="Invalid\nSelection")
    except ValueError:
        label3.config(text="Invalid Input")


def radio_used():
    print(radio_state.get())
    radio_select = radio_state.get()
    if radio_select == 1:
        label1.config(text="Miles")
        label4.config(text="Km")
    elif radio_select == 2:
        label1.config(text="Cm")
        label4.config(text="Meter")
    elif radio_select == 3:
        label1.config(text="Meter")
        label4.config(text="Inch")
    elif radio_select == 4:
        label1.config(text="Foot")
        label4.config(text="Inch")


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
mile_to_km_radiobutton = Radiobutton(text="Mile to Km", value=1, variable=radio_state, command=radio_used)
mile_to_km_radiobutton.grid(column=0, row=1)
cm_to_m_radiobutton = Radiobutton(text="CM to Meter", value=2, variable=radio_state, command=radio_used)
cm_to_m_radiobutton.grid(column=1, row=1)
m_to_inch_radiobutton = Radiobutton(text="Meter to INCH", value=3, variable=radio_state, command=radio_used)
m_to_inch_radiobutton.grid(column=0, row=2)
feet_to_inch_radiobutton = Radiobutton(text="Foot to INCH", value=4, variable=radio_state, command=radio_used)
feet_to_inch_radiobutton.grid(column=1, row=2)

label0 = Label(text="CONVERSION :-")
label0.grid(column=0, row=3)

convert_entry = Entry(width=10)
convert_entry.grid(column=1, row=3)

label1 = Label(text="Select a RB")
label1.grid(column=2, row=3)
label1.config(pady=15)

label2 = Label(text="is equal to")
label2.grid(column=0, row=4)
label2.config(pady=5)

label3 = Label(width=10, text="0")
label3.grid(column=1, row=4)
label3.config(pady=5)

label4 = Label(text="Select a RB")
label4.grid(column=2, row=4)
label4.config(pady=5)

button = Button(text="Calculate", command=calculate_conversion)
button.grid(column=1, row=5)
button.config(pady=5)

window.mainloop()
