from tkinter import *

def click():
  print("You clicked the button")

window = Tk()
button = Button(window,
                text = "Click Me",
                command=click,
                font=("Comic Mono",16),
                fg="Blue",
                bg="yellow",
                activeforeground='blue',
                activebackground='yellow',
                
                state=ACTIVE
              )
button.pack()


window.mainloop()