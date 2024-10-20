from tkinter import *

window = Tk()

def copy_text():
  input_user = entry.get()
  text_widget.insert(END,input_user + "\n")

entry = Entry(
  window,
)
entry.pack()

copy_btn = Button(
  text="COPY",
  command=copy_text
)
copy_btn.pack()


text_widget = Text(window, height=10, width=40)
text_widget.pack(pady=10)



window.mainloop()