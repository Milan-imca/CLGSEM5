import tkinter as tk
from tkinter import messagebox

# Function to handle "New" option
def new_file():
    print("New File option selected!")

# Function to handle "Open" option
def open_file():
    print("Open File option selected!")

# Function to display help information in a message box
def show_help():
    messagebox.showinfo("Help", "This is the Help information for this application.")

# Create the main window
root = tk.Tk()
root.title("Menu Example")
root.geometry("400x300")

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a "File" menu with "New" and "Open" options
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)

# Add the "File" menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Create a "Help" menu with an option to show help information
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)

# Add the "Help" menu to the menu bar
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the menu bar for the root window
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
