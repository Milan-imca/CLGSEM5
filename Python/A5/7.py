from tkinter import *

window = Tk()
window.title("List")

subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography", "Computer Science"]


listbox = Listbox(window,height=5,width=50)
listbox.pack(side="left",fill="both")

for subject in subjects:
	listbox.insert(END,subject)

scrollbar = Scrollbar(window,command=listbox.yview)
scrollbar.pack(side="left",fill=Y)

listbox.config(yscrollcommand=scrollbar.set)


window.mainloop()