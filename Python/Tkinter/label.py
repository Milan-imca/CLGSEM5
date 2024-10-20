from tkinter import *

window = Tk() 
# window.geometry("200x200")
# photo = PhotoImage(file="img.jpg")
label = Label(
    window,
    text="Milan",
    font=('Monolisa',20,'bold'),
    fg='green',
    bg='black',
    relief=SUNKEN,
    bd=10,
    padx=10,
    pady=10,
    # image=photo,
    # compound='bottom'
  )
# label.place(x=0,y=0)
label.pack()

window.mainloop() 