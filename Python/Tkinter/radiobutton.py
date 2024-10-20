# from tkinter import * 

# editors = ["Vs Code","Sublime","Replit"]

# def selection():
#   if x.get()==0:
#     print("Vs Code selected")
#   elif x.get()==1:
#     print("Sublime selected")
#   elif x.get()==2:
#     print("Replit selected")
#   else:
#     print("Oops :(")

# window = Tk()

# x = IntVar()

# for index in range(len(editors)):
#   radiobutton = Radiobutton(
#     window,
#     text=editors[index],
#     variable=x,
#     value=index,
#     command=selection
#   )
#   radiobutton.pack(anchor=W)


# window.mainloop()



from tkinter import *



editors = ["Vs Code","Sublime","Replit"]

def selection():
  selectedtext = editors[x.get()]
  selectedradio.config(text=f"selected : {selectedtext}")

window = Tk()

x = IntVar()

for index in range(len(editors)):
  radiobutton = Radiobutton(
    window,
    text = editors[index],
    variable = x,
    value= index,
    command= selection
    
  )
  radiobutton.pack(anchor=W)
  
selectedradio = Label(
  window,
  text="Selected:None"
)
selectedradio.pack()
  
window.mainloop()