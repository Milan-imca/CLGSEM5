from tkinter import *
from tkinter import messagebox

# Function to display selected options
def print_selected():
    selected_items = []
    for var, item in zip(check_vars, items):
        if var.get() == 1:  # Check if the item is selected
            selected_items.append(item)

    if selected_items:
        messagebox.showinfo("Selected Items", f"You selected: {', '.join(selected_items)}")
    else:
        messagebox.showinfo("Selected Items", "No items selected.")

# Create the main window
root = Tk()
root.title("Online Clothing Store")

# Frame to hold the check buttons
frame = Frame(root)
frame.pack(padx=20, pady=20)

# List of items (you can add more items as needed)
items = ["T-shirt", "Jeans", "Jacket", "Shoes", "Hat"]

# Create a list to hold the IntVar for each check button
check_vars = []

# Create and add check buttons to the frame
for item in items:
    var = IntVar()  # Variable to track the state of the check button
    check_vars.append(var)
    check_button = Checkbutton(frame, text=item, variable=var)
    check_button.pack(anchor="w")

# Button to print selected items
button = Button(root, text="Print Selected", command=print_selected)
button.pack(pady=10)

# Start the main loop
root.mainloop()
