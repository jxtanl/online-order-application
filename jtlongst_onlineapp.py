# Jessica Longstreth, CIS 345 T/Th 12:00-1:15 PM, A6

from tkinter import *
from PIL import Image, ImageTk
import time
from os import path
import csv

orders=[]

win=Tk()
win.title('Greeting')
win.geometry('400x600')
win.columnconfigure(0, weight=1)
win.config(bg='black')

checkvars = [IntVar() for _ in range(8)]

canvas = Canvas(win, width=300, height=180, bg='black')
canvas.grid(columnspan=3, pady=10)

logo = Image.open('coffeeshop.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0, pady=10)

logo = Image.open('coffeeshop.png')
new_width = 300
new_height = 150
img = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
img.save('coffeeshop.png')
logo = ImageTk.PhotoImage(img)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0, pady=10)

greeting_label = Label(win, text="Welcome to Bottle Coffee", fg="white", bg="black",
                       font=("Arial", 18), width=30)
greeting_label.grid(columnspan=3, padx=10, pady=10)

price_info_label = Label(win, text="Order Form *Every item is $5.50", fg="white", bg="black",
                         font=("Arial", 14), width=30)
price_info_label.grid(columnspan=3, padx=10, pady=10)

box1 = Frame(win, bg='white', width=280, height=200,
borderwidth=5, relief=RIDGE)
box1.grid(row=4, column=0, columnspan=3)
box1.grid_propagate(False)
box1.columnconfigure(0, weight=1)
box1.columnconfigure(1, weight=1)

c1 = Checkbutton(box1, text="Iced Mint Mojito", fg='#6f4e37', bd=10, variable=checkvars[0],
                 font=("Arial", 16), onvalue=1, offvalue=0)
c1.grid(row=1, column=0, pady=2, sticky=W)

checkbox_texts = [
    "Iced Mint Mojito",
    "Iced Samatra",
    "Iced Black",
    "Hot Black",
    "Bottle Burger",
    "Bottle Fries",
    "Bottle Ice Cream",
    "Bottle Muffin"
]

for i, text in enumerate(checkbox_texts):
    c = Checkbutton(box1, text=text, fg='#6f4e37', bd=10, variable=checkvars[i],
                    font=("Arial", 16), onvalue=i+1, offvalue=0)
    c.grid(row=(i // 2) + 1, column=i % 2, pady=2, sticky=W)

name_label = Label(win, text="Enter your name: ", fg="white", bg="black", font=("Arial", 16), width=30)
name_label.grid(column=0, row=7, pady=10, padx=10, columnspan=3, sticky=EW)

name_entry = Entry(win, justify=CENTER, font=("Arial", 16), bg="white", fg="black")
name_entry.grid(column=0, row=8, pady=10, padx=10, columnspan=3, sticky=N)

total_charge_label = Label(win, text="Hello", fg="black", bg="white", font=("Arial", 16), width=30)
total_charge_label.grid(column=0, row=9, pady=10, padx=10, columnspan=3)

def clear_checkboxes():
    global orders, name_entry
    for var in checkvars:
        var.set(0)
    orders = []
    name_entry.delete(0, END)

def button_click():
    global orders, name_entry, total_charge_label
    customer_name = name_entry.get()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    if not path.isfile('orders.txt'):
        with open('orders.txt', 'w') as file:
            file.write('Bottle Coffee Ordering Records: \n')

    if not path.isfile('orders.csv'):
        with open('orders.csv', 'w', newline='') as fp:
            data = csv.writer(fp)
            data.writerow(['Name', 'Time', 'Orders', 'Total Price'])

    orders = [var.get() for var in checkvars]
    orders = list(filter(None, orders))
    cost = len(orders) * 5.5

    with open('orders.txt', 'a') as file:
        order_details = f"{customer_name}, {current_time}, {orders}, ${cost:.2f}\n"
        file.write(order_details)

    with open('orders.csv', 'a', newline='') as fp:
        data = csv.writer(fp)
        orderstring = ' '.join(str(order) for order in orders)
        data.writerow([customer_name, current_time, orderstring, f"${cost:.2f}"])

    first_name = customer_name.split()[0] if customer_name else "Customer"
    total_charge_label.config(text=f"Thank you {first_name}, total cost is ${cost:.2f}!")

    clear_checkboxes()

def close():
    win.destroy()

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)

submit_button = Button(win, command=button_click, font=("Arial", 16), text='Submit', width=15)
submit_button.grid(column=1, row=10, pady=20, padx=(10, 5), sticky='W')

exit_button = Button(win, command=close, font=("Arial", 16), text='Exit', width=15)
exit_button.grid(column=1, row=10, pady=20, padx=(5, 10), sticky='E')

win.grid_propagate(False)

win.mainloop()



