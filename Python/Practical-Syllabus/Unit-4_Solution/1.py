# Create a GUI Application to demonstrate working of calculator using Tkinter. 

from tkinter import *

window = Tk()
window.title("Calculator")

expression = ""

def on_button_click(char):
  global expression
  if char == 'C':
    expression = ""
  elif char == '=':
    try:
      expression = str(eval(expression))
    except Exception:
      expression = "Error"
  else:
    expression += char
  
  input_text.set(expression)
  
input_text = StringVar()

input_frame = Frame(window)
input_frame.pack()

input_field = Entry(input_frame,textvariable=input_text,font=('Dank Mono',20),bd=10,insertwidth=4,width=14,borderwidth=4)
input_field.grid(row=0,column=0,columnspan=4)

button_frame = Frame(window)
button_frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text,row,col) in buttons:
  button = Button(button_frame,text=text,padx=20,pady=20,font=('Monolisa',20),command= lambda t=text: on_button_click(t))
  button.grid(row=row,column=col)
  
window.mainloop()