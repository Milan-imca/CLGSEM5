#Entry widget takes single line input(textbox)
from tkinter import * 

def on_submit():
  username = name.get()
  pswd = password.get()
  
  print(f"Hii {username}")
  print(f"Password : {pswd}")

window = Tk()

name = Entry(
  window,
  font=("Comic Mono",16)
)
name.pack()


password = Entry(
  window,
  font=("Comic Mono",16),
  show="*"
)
password.pack()

submit_button = Button(
  window,
  text="Submit",
  command=on_submit
)

submit_button.pack()

window.mainloop()