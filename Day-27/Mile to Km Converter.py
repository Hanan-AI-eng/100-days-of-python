from tkinter import *

#create a window + title added
window=Tk()
window.minsize(width=200,height=100)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

#method to calculate
def mile_to_km():
    mile=calculate_entry.get()
    mile_flout=float(mile)
    km=float(mile_flout * 1.60934)

    num.config(text=round(km))

# create an Entry
calculate_entry=Entry(width=8)
calculate_entry.grid(column=2,row=1)

# titles
Mile_title=Label(text="Miles")
Mile_title.grid(column=3,row=1)

equal=Label(text="is equal to")
equal.grid(column=0,row=2)

num=Label(text=0)
num.grid(column=2,row=2)

Km=Label(text="Km")
Km.grid(column=3,row=2)

#button
Calculate_button=Button(text="Calculate",command=mile_to_km)
Calculate_button.grid(column=2,row=3)

window.mainloop()