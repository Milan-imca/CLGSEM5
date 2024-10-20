from tkinter import *

window = Tk()


def submit():
  user_name = name.get()
  display.config(text=f"\nName : {user_name}")

Label(text="Enter name : ").grid(row=0,column=0)
name = Entry(window)
name.grid(row=0,column=1)

Button(text="Submit",command=submit).grid(row=1,columnspan=2)

display = Label(window,text="")
display.grid(row=3,column=0)

window.mainloop()