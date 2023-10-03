import tkinter as tk
from tkinter import ttk

# Function to add an expense
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = float(amount_entry.get())

    # Update the total expense
    total_expense.set(total_expense.get() + amount)

    # Add the expense to the listbox
    expense_listbox.insert(tk.END, f"{date} - {category} - ${amount:.2f}")


app = tk.Tk()
app.title('Expense Tracker')

# Initvariables
total_expense = tk.DoubleVar()
total_expense.set(0.0)

#  labels and entry fields
date_label = ttk.Label(app, text='Date:')
date_label.pack()

date_entry = ttk.Entry(app)
date_entry.pack()

category_label = ttk.Label(app, text='Category:')
category_label.pack()

category_entry = ttk.Entry(app)
category_entry.pack()

amount_label = ttk.Label(app, text='Amount ($):')
amount_label.pack()

amount_entry = ttk.Entry(app)
amount_entry.pack()

# button to add expenses
add_button = ttk.Button(app, text='Add Expense', command=add_expense)
add_button.pack()

# listbox to display expenses
expense_listbox = tk.Listbox(app, height=10, width=50)
expense_listbox.pack()

# label to display the total expense
total_label = ttk.Label(app, textvariable=total_expense)
total_label.pack()

app.mainloop()