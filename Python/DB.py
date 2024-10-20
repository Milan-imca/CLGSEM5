from tkinter import *
import mysql.connector
from tkinter import messagebox

    
window = Tk()
window.geometry("500x600")

def on_submit():
  e_id = id.get()
  e_name = name.get()
  e_dep = dep.get()
  
  
  try:
    connection = mysql.connector.connect(
      host="localhost",
      username="root",
      password="123456",
      database="milan"
    )
    
    if connection.is_connected():
      print("Connection Success!")
      
      cursor = connection.cursor()
      
      sql = "INSERT INTO  emp_details (id,name,dep) values (%s,%s,%s)"
      data = (e_id,e_name,e_dep)
      
      cursor.execute(sql,data)
      connection.commit()
      
      messagebox.showinfo("Success","Data Inserted")
    
    else:
      print("connection failed")
      
  except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert data: {error}")
    
    
    
    
    
    
def clear():
  name.delete(0,END)
  id.delete(0,END)
  dep.delete(0,END)

def fetch_data():
  try:
    connection = mysql.connector.connect(
      host="localhost",
      username="root",
      password="123456",
      database="milan"
    )
    
    if connection.is_connected():
      print("Connection Success!")

      connection_cursor = connection.cursor()
      sql = "SELECT * FROM emp_details"
      connection_cursor.execute(sql)
      records = connection_cursor.fetchall()
      
      texts.delete('1.0',END)
      
      for row in records:
        texts.insert(END,f"ID : {row[0]} NAME : {row[1]} DEPARTMENT : {row[2]}\n")
    
  except mysql.connector.Error as e:
    print(f"Error {e}")
      


def update():
  choice.set(None)
  options_label.grid(row=10,column=0)
  radio_name.grid(row=11,column=1)
  confirm_btn.grid(row=12,column=1)
  
  
def change():
  update_name_label.grid(row=13,column=1)
  user_name.grid(row=13,column=2)
  final_confirm_btn.grid(row=13,column=3)
  

def final_change():
  emp_id = user_id.get()
  updated_value = user_name.get()
  field_to_update = choice.get()
  print(field_to_update)
  
  if field_to_update == "name":
    update_query = "UPDATE emp_details SET name = %s WHERE id = %s "
  else:
    messagebox.showwarning("Warning", "Please select a valid option to update.")
    return
  
  try:
    connection = mysql.connector.connect(
      host = "localhost",
      username = "root",
      password = "123456",
      datbase = "milan"
    )
    
    if connection.is_connected():
      cursor = connection.cursor()
      cursor.execute(update_query,(updated_value,emp_id))
      connection.commit()
      messagebox.showinfo("Success",f"Update succesfull")
      
  except mysql.connection.Error as e:
    print(f"Error {e}")
    
Label(text="Employee Details").grid(row=0,column=1)
Label(text="Name : ").grid(row=1,column=0)
name = Entry(window)
name.grid(row=1,column=1,pady=10,padx=10)

Label(text="Id : ").grid(row=2,column=0)
id = Entry(window)
id.grid(row=2,column=1,pady=10,padx=10)

Label(text="Deparment : ").grid(row=3,column=0)
dep = Entry(window)
dep.grid(row=3,column=1,pady=10,padx=10)

Button(text="Submit",command=on_submit).grid(row=4,column=1,padx=5,pady=5)

Button(text="Clear",command=clear).grid(row=5,column=1,padx=5,pady=5)

Button(text="Fetch Data",command=fetch_data).grid(row=6,column=1,padx=5,pady=5)


texts = Text(window,height=10,width=50)
texts.grid(row=7,columnspan=5,padx=10,pady=10)


Label(text="Data update").grid(row=8,column=0)
Label(text="Enter id").grid(row=9,column=0)
user_id = Entry(window)
user_id.grid(row=9,column=1)

Button(text="Go to update",command=update).grid(row=9,column=2)

choice = StringVar()

options_label = Label(text="Select the option you want to udpate")
radio_name = Radiobutton(window,text="Name",variable=choice,value=name)

confirm_btn = Button(window,text="Confirm Update",command=change)
update_name_label = Label(text="Enter name for updation")
user_name = Entry(window)


final_confirm_btn = Button(window,text="Final Update",command=final_change)

window.mainloop()