# Develop a Tkinter application with three Buttons: one 
# to display a message in a Label, one to
# change the Label text, and one to exit the application.

# 3-> button, label (display,change,exit)

from tkinter import *

window = Tk()

def display_label():
  label.config(text="Label Displayed")

def change_label():
  label.config(text="Label Changed!!")

def exit_app():
  window.destroy()

label = Label(text="")
label.pack()

display_btn = Button(
  text="Display label",
  command=display_label
)
display_btn.pack()

change_btn = Button(
  text="Change label",
  command=change_label
)
change_btn.pack()

exit_btn = Button(
  text="Exit app",
  command=exit_app
)
exit_btn.pack()

window.mainloop()