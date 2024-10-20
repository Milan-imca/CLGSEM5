# Create a Student Registration form for library.
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Library Registration Form")


Label(window,text="Student name : ").grid(row=0,column=0,padx=10,pady=10)
student_name = Entry(window)
student_name.grid(row=0,column=1,padx=10,pady=10)

Label(window,text="Student ID:").grid(row=1,column=0,padx=10,pady=10)
student_id = Entry(window)
student_id.grid(row=1,column=1,padx=10,pady=10)

Label(window,text="Select Course :").grid(row=2,column=0,padx=10,pady=10)
course_var = StringVar(value="IMCA")

Radiobutton(window,text="IMCA",variable=course_var,value="IMCA").grid(row=2,column=1,sticky='w')
Radiobutton(window,text="BCA",variable=course_var,value="BCA").grid(row=3,column=1,sticky='w')
Radiobutton(window,text="IMScIT",variable=course_var,value="BCA").grid(row=4,column=1,sticky='w')

Label(window,text="Phone number : ").grid(row=5,column=0,padx=10,pady=10)
phone_number = Entry(window)
phone_number.grid(row=5,column=1,padx=10,pady=10)


def submit_form():
	id = student_id.get()
	name = student_name.get()
	selected_course = course_var.get()
	p_number = phone_number.get()

	if not id or not name or not selected_course or not p_number:
		messagebox.showerror("Input Error","Please fill out all the details")
		return

	messagebox.showinfo("Registration Success!!",f"Id : {id}\nName : {name}\nSelected Course : {selected_course}\nPhone Number : {p_number}")

Button(window,text="SUBMIT",command=submit_form).grid(row=6,columnspan=2,pady=20)

window.mainloop()

