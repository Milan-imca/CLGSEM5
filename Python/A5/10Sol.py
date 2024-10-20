from tkinter import *
from tkinter import messagebox
def new():
  print("new")
  
def help():
  messagebox.showinfo("Info","Help")

window = Tk()

window.geometry("500x500")

menu_bar = Menu(window)

menu_option = Menu(menu_bar,tearoff=0)
menu_option.add_command(label="new",command=new)
menu_bar.add_cascade(label="FILE",menu=menu_option)

help_menu_option = Menu(menu_bar,tearoff=0)
help_menu_option.add_command(label="Help",command=help)
menu_bar.add_cascade(label="Help",menu=help_menu_option)

window.config(menu=menu_bar)

window.mainloop()