from tkinter import *

def show_entry():
  print("Entry content : ",entry.get())
  cbv = check_var.get()
  if cbv == 1:
    print("Selected")
  else:
    print("Not Selected")
  print("Checkbox content ")
  rv = radio_var.get()
  print(f"Selected radio : {rv}")
  lv =listbox.curselection()
  print("Listbox selection : ",lv)

root = Tk()

label = Label(root,text="Enter something")
label.pack()

entry = Entry(root)
entry.pack()

check_var = IntVar()
checkbutton = Checkbutton(root,text="Check me",variable=check_var)
checkbutton.pack()

radio_var = StringVar(value="Option 1")
rb1 = Radiobutton(root,text="Option 1",variable=radio_var,value="Option 1")
rb2 = Radiobutton(root,text="Option 2",variable=radio_var,value="Option 2")
rb1.pack()
rb2.pack()


listbox = Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()


button = Button(root,text="Show Data",command=show_entry)
button.pack()

root.mainloop()