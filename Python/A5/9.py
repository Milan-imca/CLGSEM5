# Create a Tkinter window with a Button that, when clicked, displays a MessageBox with a custom message and an OK button. Use multiple buttons to display instance of each type of Message Box.

from tkinter import *
from tkinter import messagebox

def ask_question():
	response = messagebox.askquestion("Question","Do you like tkinter")
	if response == 'yes':
		messagebox.showinfo("Response","That's Great!!")
	else:
		messagebox.showinfo("Response","Oops!!!")

def show_info():
	messagebox.showinfo("Message","Hii User!!")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")

# Function to display an error message box
def show_error():
    messagebox.showerror("Error", "This is an error message!")

window = Tk()
window.geometry("300x300")

ask_btn = Button(window,text="ASK QUESTION",command=ask_question,padx=2,pady=2)
ask_btn.pack(padx=3,pady=3)


show_info_btn = Button(window,text="SHOW MESSAGE",command=show_info,padx=2,pady=2)
show_info_btn.pack(padx=3,pady=3)

warning_button = Button(window, text="Show Warning", command=show_warning)
warning_button.pack(pady=10)

error_button = Button(window, text="Show Error", command=show_error)
error_button.pack(pady=10)

window.mainloop()