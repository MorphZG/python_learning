""" importing everything from tkinter although it is a bad practice """

from tkinter import *


def convert_km_mile():
    # 1 mile == 1.60934 km
    miles = float(input_field.get())
    kilometers = miles * 1.609
    label2.config(text=kilometers)
    print('Converted!')


window = Tk()
window.title('Miles to Kilometer Converter')
#window.minsize(width=300, height=200)
window.config(padx=20, pady=20)  # padding

# label1
label1 = Label(text='is equal to', font=('Arial', 10))
label1.grid(column=0, row=1)

# label2
label2 = Label(text='0', font=('Arial', 10))
label2.grid(column=1, row=1)

# label
label3 = Label(text='Km', font=('Arial', 10))
label3.grid(column=2, row=1)

# label
label4 = Label(text='Miles', font=('Arial', 10))
label4.grid(column=2, row=0)

# button
button = Button(text='Convert', command=convert_km_mile)
button.grid(column=1, row=2)

# entry
input_field = Entry(width=10)
input_field.grid(column=1, row=0)


window.mainloop()



#modules: tkinter
#tags: widget, pack(), grid(), converter
