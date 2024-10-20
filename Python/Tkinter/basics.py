from tkinter import * 

window = Tk() 
window.title("Tkinter basics")


# label widget
label = Label(window,text="Hello,tkinter")
# label.pack()
label.grid(row=0,column=0)

def on_button_clicked():
  print("Button Clicked")

# button widget
button = Button(window,text="Click me",command=on_button_clicked)
# button.pack()
button.grid(row=1,columnspan=2)


# entry widget
entry = Entry(window)
# entry.pack()
entry.grid(row=0,column=1)

# text : multi-line input
# text = Text(window,height=5,width=20)
# text.pack()

#  => Checkbox
# check_var = IntVar()
# checkbutton = Checkbutton(window,text="Check me",variable=check_var)
# checkbutton.pack()


# => Radio button
# radio_var = StringVar(value="Option 1")
# rb1 = Radiobutton(window,text="Option 1",variable=radio_var,value="Option 1")
# rb2 = Radiobutton(window,text="Option 2",variable=radio_var,value="Option 2")
# rb1.pack()
# rb2.pack()

# Listbox 
# listbox = Listbox(window)
# listbox.insert(1,"Item 1")
# listbox.insert(2,"Item 2")
# listbox.pack()



window.mainloop()