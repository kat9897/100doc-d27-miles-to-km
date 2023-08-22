from tkinter import *

windows = Tk()
windows.title("Miles to Km Converter")
windows.minsize(width=250, height=100)
windows.config(padx=35, pady=20)

# Col 0
# Label - is equal to
equal = Label(text="is equal to")
equal.grid(column=0, row=1)

# Col 1
# Entry - Miles number
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Label - Km number
km_num = 0
km_num_label = Label(text=km_num)
km_num_label.grid(column=1, row=1)


# Button - Calculate
def miles_to_km():
    miles = entry.get()
    km = round(float(miles) * 1.60934)
    km_num_label.config(text=str(km))


calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

# Col 2
# Label - Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label - Km
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

windows.mainloop()
