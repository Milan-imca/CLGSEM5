from tkinter import *

def display():
  if x.get() == 1:
    print("Yeah! you accepted the terms.")
  else:
    print("Oops! You didn't accepted the terms.")


window = Tk()

x = IntVar()

check = Checkbutton(
  window,
  text="Accept the terms",
  variable=x,
  onvalue=1,
  offvalue=0,
  command=display
)

check.pack()
window.mainloop()