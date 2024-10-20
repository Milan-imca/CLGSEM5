# Create a GUI Application to find odd/even on Button Click. 

from tkinter import * 

window = Tk()

entry = Entry(window,font=("Arial",16))
entry.pack()

def check_odd_or_even():
  value = int(entry.get())
  if value % 2 == 0:
    label.config(text=f"{value} is EVEN")
  else:
    label.config(text=f"{value} is ODD")

check_button = Button(
  window,
  text="Check ODD or EVEN",
  font=("Arial",12),
  command=check_odd_or_even
  )
check_button.pack(pady=5)

label = Label(window,
              text="",
              font=("Arial",16)
              )
label.pack()

window.mainloop()