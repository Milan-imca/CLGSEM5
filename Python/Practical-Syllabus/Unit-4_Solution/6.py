# Create a GUI Application to count Button Click.
from tkinter import * 

window = Tk()

count = 0

def increment():
  global count
  count += 1
  label.config(text=f"Button Clicked Count : {count}")


def reset():
  global count
  count = 0
  label.config(text=f"Button Clicked Count : {count}")

label = Label(window,text=f"Button Clicked Count : {count}",font=("Arial",20))
label.pack(pady=20)

increment_btn = Button(window,text="INCREMENT",command=increment,bg="green")
increment_btn.pack(pady=20)

reset_btn = Button(window,text="RESET",command=reset,bg="red")
reset_btn.pack(pady=20)

window.mainloop()

