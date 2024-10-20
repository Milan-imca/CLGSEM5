from tkinter import *
from tkinter import messagebox



def  selected_items():
	selected_items = []
	for var,item in zip(check_vars,item_list):
		if var.get() == 1:
			selected_items.append(item)

	if selected_items:
		messagebox.showinfo("Selected Items",f"Cart items : {','.join(selected_items)}")
	else:
		messagebox.showinfo("Selected Items",f"No items selected!!")


window = Tk()
window.title("Online Shopping")

frame = Frame(window)
frame.pack(padx=20,pady=20)

check_vars = []

item_list = ['Hoodie','sweatshirt']

for item in item_list:
	var = IntVar()
	check_vars.append(var)
	check_button = Checkbutton(frame,text=item,variable=var)
	check_button.pack(anchor='w')

Button(text="Go to Cart",command=selected_items).pack()

window.mainloop()

