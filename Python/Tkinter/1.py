# 1
# from tkinter import *
# window = Tk()
# window.geometry("400x400")
# text = Label(
# 	window,
# 	text="Welcome To Tkinter!",
# 	font=("Comic Mono",16),
# 	fg="red"
# 	)
# text.pack()

# window.mainloop() 

# 2

# from tkinter import *

# def display_message():
# 	label.config(text="Hello",fg="red")

# def change_label():
# 	label.config(text="Hii,there",fg="green")

# def exit_app():
# 	window.destroy()

# window = Tk() 
# window.geometry("400x400")

# label = Label(
# 	window,
# 	text="",
# 	font=("Comic Mono Sans",12),
# 	)
# label.pack()


# display_button = Button(
# 	window,
# 	text="Display message",
# 	command=display_message
# 	)
# display_button.pack()

# change_button = Button(
# 	window,
# 	text="Change Button",
# 	command = change_label
# 	)
# change_button.pack()

# exit_button = Button(
# 	window,
# 	text="Exit",
# 	command=exit_app
# 	)
# exit_button.pack()

# window.mainloop()


import tkinter as tk

# Function to print selected options
def print_selected_options():
    selected_options = []
    for index, var in enumerate(check_vars):
        if var.get():  # Check if the Checkbutton is selected
            selected_options.append(clothing_options[index])
    print("Selected options:", selected_options)

# Create the main window
window = tk.Tk()
window.title("Online Clothing Store")

# Set window size
window.geometry("300x300")

# Clothing options
clothing_options = [
    "T-Shirt",
    "Jeans",
    "Jacket",
    "Sweater",
    "Shorts",
    "Hat"
]

# Variable list to hold the state of each Checkbutton
check_vars = []

# Create a Frame to hold the Checkbuttons
frame = tk.Frame(window)
frame.pack(pady=20)

# Create Checkbuttons for each clothing option
for option in clothing_options:
    var = tk.IntVar()  # Create a variable to hold the state of each Checkbutton
    check_vars.append(var)  # Add the variable to the list
    check_button = tk.Checkbutton(frame, text=option, variable=var)
    check_button.pack(anchor='w')  # Pack Checkbuttons in a vertical list

# Create a Button to print selected options
print_button = tk.Button(window, text="Print Selected Options", command=print_selected_options)
print_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()